from io import StringIO


def makeIndentString(indentStr, level=0):
    out = ""
    if indentStr is not None:
        out = "\n" + (indentStr * level)
    return out


def writerFor(obj):
    return {
        dict: writeDict,
        list: writeList,
        str: writeString,
        int: writeInteger,
        bool: writeBoolean
    }[type(obj)]


def write(obj, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    indStr = makeIndentString(indentStr, level)
    pos = outstream.tell()
    outstream.write(
        '<?xml version="1.0" encoding="UTF-8"?>\n' +
        '<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    )
    outstream.write('\n<plist version="1.0">')
    writeObject(obj, outstream, indentStr, level)
    outstream.write('\n</plist>')
    outstream.seek(pos)
    return outstream


def writeObject(obj, outstream=None, indentStr=None, level=0):
    """
    Writes an object to an output stream
    """
    outstream = outstream or StringIO()
    return writerFor(obj)(obj, outstream, indentStr, level)


def writeList(listObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    indentString = makeIndentString(indentStr, level)
    outstream.write("{}<array>".format(indentString))
    for value in listObject:
        writeObject(value, outstream, indentStr, level + 1)
    outstream.write("{}</array>".format(indentString))
    return outstream


def writeDict(dictObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    indentString = makeIndentString(indentStr, level)
    outstream.write("{}<dict>".format(indentString))
    for key, value in dictObject.items():
        writeKey(key, outstream, indentStr, level + 1)
        writeObject(value, outstream, indentStr, level + 1)
    outstream.write("{}</dict>".format(indentString))
    return outstream


def writeBoolean(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    outstream.write("{}<{}/>".format(makeIndentString(indentStr, level),
                                     ("true" if value else "false")))
    return outstream


def writeKey(key, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    outstream.write("{}<key>{}</key>".format(
        makeIndentString(indentStr, level), str(key)))
    return outstream


def writeString(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    outstream.write("{}<string>{}</string>".format(
        makeIndentString(indentStr, level), value))
    return outstream


def writeInteger(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or StringIO()
    outstream.write("{}<integer>{}</integer>".format(
        makeIndentString(indentStr, level), str(value)))
    return outstream
