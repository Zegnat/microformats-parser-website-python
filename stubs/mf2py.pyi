"""Type stubs for mf2py."""

from collections import OrderedDict
from typing import IO, TypedDict

class Mf2Item(TypedDict, total=False):
    type: list[str]
    properties: dict[str, list[object]]
    children: list["Mf2Item"]
    value: str
    lang: str

class Mf2Debug(TypedDict):
    description: str
    source: str
    version: str

class Mf2Result(TypedDict):
    items: list[Mf2Item]
    rels: dict[str, list[str]]
    debug: Mf2Debug

class Parser:
    user_agent: str
    dict_class: type[OrderedDict[str, object]]

__version__: str

def parse(
    doc: str | IO[str] | None = None,
    url: str | None = None,
    html_parser: str | None = None,
    expose_dom: bool = False,
    metaformats: bool = False,
    filter_roots: bool = False,
) -> Mf2Result: ...
