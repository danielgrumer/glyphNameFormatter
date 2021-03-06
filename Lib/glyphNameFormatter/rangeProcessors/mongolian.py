
def process(self):
    # edits go here
    self.edit("MONGOLIAN")
    self.edit("DIGIT")

    self.replace("FULL STOP", "period")

    parts = [
        "TODO", "SIBE", "MANCHU", "ALI GALI", "HALF", "THREE",

        "INVERTED",
        ]
    for part in parts:
        self.edit(part, part.lower().replace(" ", ""))

    self.replace("LETTER")

    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Mongolian")
