
def process(self):
    # If the Arabic ligature names comes with any of these terms then these rules apply on components:

    # Initial ligature: FIRST component is INIT and the REST are MEDI
    # Medial ligature: ALL the components are MEDI
    # Final ligature: the LAST component is FINA and the rest are MEDI
    # Isolate ligature: The LAST components is FINA, the fist components is INIT and the rest are MEDI

    if self.has("LIGATURE"):
        self.processAs("Helper Arabic Ligature")
    else:
        self.processAs("Arabic")


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Arabic Presentation Forms-A")
