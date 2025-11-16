# -*- coding: utf-8 -*-
# This file is part of AYAB.
#
#    AYAB is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AYAB is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AYAB.  If not, see <http://www.gnu.org/licenses/>.
#
#    Copyright 2014 Sebastian Oliva, Christian Obersteiner,
#       Andreas Müller, Christian Gerbrandt
#    https://github.com/AllYarnsAreBeautiful/ayab-desktop
"""
Module providing abstraction layer for user preferences.

User preferences are configured on startup.
The method of configuration may differ depending on the OS.
"""

from __future__ import annotations

from .signal_sender import SignalSender
from .engine.options import Alignment
from .engine.mode import Mode
from .machine import Machine
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Literal,
    Optional,
    TypeAlias,
    TypeVar,
    TypedDict,
    cast,
    overload,
)

if TYPE_CHECKING:
    from .ayab import GuiMain

T = TypeVar("T")


def str2bool(qvariant: str | bool) -> bool:
    if type(qvariant) is str:
        return qvariant.lower() == "true"
    else:
        return cast(bool, qvariant)


PreferencesDictBoolKeys: TypeAlias = Literal[
    "default_infinite_repeat",
    "default_knit_side_image",
    "quiet_mode",
    "disable_hardware_beep",
]
PreferencesDictIntKeys: TypeAlias = Literal["lower_display_stitch_width"]
PreferencesDictObjKeys: TypeAlias = Literal[
    "aspect_ratio", "default_alignment", "default_knitting_mode", "machine"
]
PreferencesDictKeys: TypeAlias = Literal[
    PreferencesDictBoolKeys, PreferencesDictObjKeys, PreferencesDictIntKeys, "language"
]

PreferencesDict = TypedDict(
    "PreferencesDict",
    {
        "machine": type[Machine],
        "default_knitting_mode": type[Mode],
        "default_infinite_repeat": type[bool],
        "default_alignment": type[Alignment],
        "default_knit_side_image": type[bool],
        # 'default_continuous_reporting': bool,
        "quiet_mode": type[bool],
        "disable_hardware_beep": type[bool],
        "lower_display_stitch_width": type[int],
    },
)


class Preferences(SignalSender):
    """Default settings class.

    Variable names and classes are defined in the dict `variables`.
    Classes other than `bool` are expected to have a method `add_items`
    that populates a combo box. The first item (index 0) is the default.
    Language defaults to US English if there are no translations
    available for the user's locale. It is the only setting that is not
    set back to the default by the "Reset" button.

    @author Tom Price
    @date   June 2020
    """

    variables: PreferencesDict = {
        "machine": Machine,
        "default_knitting_mode": Mode,
        "default_infinite_repeat": bool,
        "default_alignment": Alignment,
        "default_knit_side_image": bool,
        # 'default_continuous_reporting': bool,
        "quiet_mode": bool,
        "disable_hardware_beep": bool,
        "lower_display_stitch_width": int,
    }

    def __init__(self, parent: GuiMain):
        super().__init__(parent.signal_receiver)
        self.parent = parent
        self.settings = self.parent.settings
        print("self.settings",self.settings)
#        self.settings.setFallbacksEnabled(False)
#        self.refresh()

    def refresh(self) -> None:
        for var in self.variables.keys():
            self.settings[var] = self.value(cast(PreferencesDictKeys, var))

    def reset(self) -> None:
        """Reset all the fields except language"""
        for var in self.variables.keys():
            if self.variables[cast(PreferencesDictKeys, var)] != Language:
                self.settings.setValue(
                    var, self.default_value(cast(PreferencesDictKeys, var))
                )

    @overload
    def value(self, var: PreferencesDictBoolKeys) -> bool: ...
    @overload
    def value(self, var: PreferencesDictIntKeys | PreferencesDictObjKeys) -> int: ...
    @overload
    def value(self, var: Literal["language"]) -> str: ...

    def value(self, var: PreferencesDictKeys) -> Any:
        if var in self.settings.keys():
            try:
                return self.convert(var)(self.settings[var])
            except ValueError:
                # saved setting is wrong type
                return self.convert(var)()  # type: ignore
        else:
            return self.default_value(var)

    def convert(self, var: PreferencesDictKeys) -> Callable[[object], Any]:
        try:
            cls = self.variables[var]
        except KeyError:
            return str
        # else
        if cls == bool:
            return cast(Callable[[object], Any], str2bool)
        # else
        return cast(Callable[[object], Any], int)

    def default_value(
        self, var: PreferencesDictKeys
    ) -> Optional[bool | str | int | Literal[0]]:
        try:
            cls = self.variables[var]
        except KeyError:
            return None
        # else
        if cls == bool:
            return False
        # else
        #if cls == Language:
        #    return self.languages.default_language()
        if cls == int:
            return 20
        # else
        return 0

    def open_dialog(self) -> None:
        machine_width = Machine(self.value("machine")).width
        PrefsDialog(self.parent).exec()
        if machine_width != Machine(self.value("machine")).width:
            self.emit_image_resizer()

