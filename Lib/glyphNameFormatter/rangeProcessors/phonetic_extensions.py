from glyphNameFormatter.data.scriptPrefixes import addScriptPrefix


def process(self):
    # edits go here
    self.edit("LATIN")

    self.edit("WITH")

    parts = [
        "OPEN", "STROKE", "TURNED", "REVERSED",
        "SIDEWAYS", "SUBSCRIPT",
        "TOP", "BOTTOM",
        "RETROFLEX", "SCRIPT",
        "HALF", "INSULAR",
        "VOICED", "LARYNGEAL",
        ]
    for part in parts:
        self.edit(part, part.lower())

    self.edit("BARRED", "bar")
    self.edit("STRIKETHROUGH", "strike")
    self.edit("DIAERESIZED", self.prefSpelling_dieresis+"ed")

    self.replace("SPIRANT", "spirant")
    self.replace("LAMDA", "lambda")
    self.replace("LETTER SMALL CAPITAL L", "Lsmall")
    self.replace("LETTER SMALL CAPITAL N", "Nsmall")
    self.replace("LETTER SMALL CAPITAL R", "Rsmall")
    self.replace("SMALL CAPITAL LETTER U", "Usmall")
    self.replace("SMALL CAPITAL LETTER I", "Ismall")
    self.replace("LETTER SMALL CAPITAL EL", "ELsmall")
    self.replace("AIN", "ain")

    self.replace("LETTER SMALL CAPITAL AE", "AEsmall")
    self.replace("LETTER SMALL CAPITAL OU", "OUsmall")

    self.edit("FISHHOOK AND MIDDLE TILDE", "fishmiddletilde")
    self.processDiacritics()

    if self.has("GREEK"):
        self.edit("GREEK")
        self.handleCase()
        self.uniNameProcessed = addScriptPrefix(self.uniNameProcessed, script="greek")
    elif self.has("CYRILLIC"):
        self.edit("CYRILLIC")
        self.handleCase()
        self.uniNameProcessed = addScriptPrefix(self.uniNameProcessed, script="cyrillic")
    else:
        self.handleCase()

    self.edit("MODIFIER", "mod")
    self.edit("LETTER")

    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Phonetic Extensions")
