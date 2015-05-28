import xml.sax

class pyBigXML:

    def __init__(self, xmlfile):
        self.xmlfile = xmlfile
        self.xmlh = XMLHandler()

    def parse(self):
        source = open(self.xmlfile)
        return self.xmlh.parse(source)

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.return_me = {}
        self.current = ""
        self.current_list = []
        self.depth = 0
        self._char_buff = []
    def _get_chars(self):
        chars = ''.join(self._char_buff).strip()
        self._char_buff = []
        return chars.strip()
    def _insert(self, v):
        x = self.return_me
        y = {}
        for i in range(len(self.current_list)):
          if self.current_list[i] in x:
              print "KEY EXISTS"
              x = self.return_me[self.current_list[i]]
          else:
              print "NO KEY"
              x[self.current_list[i]] = {}

    def parse(self, f):
        xml.sax.parse(f, self)
        return self.return_me
    def startDocument(self):
        print "START"
    def endDocument(self):
        print "END"
    def startElement(self, name, attrs):
      if name != "":
          self.current = name
          #print "Adding {0} name".format(name)
          #print "list {0}".format(self.current_list)
          #print self.return_me
          self.current_list.append(name)
          self.depth = self.depth + 1
    def endElement(self, name):
      if name != "":
          chars = self._get_chars()
          if len(chars) > 0:
              self._insert(chars)
              b = dict(izip(i, i))
              d = dict(itertools.izip_longest(*[iter(self.current_list))] * 2, fillvalue=""))
          self.current = ""
          self.current_list.pop()
          self.depth = self.depth - 1
    #def startElementNS(self, name, qname, attrs):
    #def endElementNS(self, name, qname):
    def characters(self, content):
        if self.current != "":
            self._char_buff.append(content)
      #print "Content {0} ".format(content)
    #def processingInstruction(self, target, data):
    #def ignorableWhitespace(self, whitespace):
    #def skippedEntity(self, name):
    #def startPrefixMapping(self, prefix, uri):
    #def endPrefixMapping(self, prefix):
    #def setDocumentLocator(self, locator):
