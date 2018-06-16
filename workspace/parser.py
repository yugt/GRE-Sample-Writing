class writing(object):
    lines = None
    outpath = None
    passages = []
    empty_line = False

    def __init__(self, inpath, outpath):
        file = open(inpath, "r")
        self.outpath = outpath
        self.lines = file.readlines()
        file.close()
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].rstrip()
            self.lines[i] = self.lines[i].replace('\x0c','')
            self.lines[i] = self.lines[i].replace('\n','')
        self.__issue()

    def __issue(self):
        temp = []
        for line in self.lines:
            if line[0:5] == "Issue":
                self.empty_line = False
                temp.append(line)
            elif len(line)==0:
                if ~self.empty_line:
                    self.empty_line = True
                    self.passages.append(temp)
                    temp = []
            else:
                temp.append(line)
        self.passages = [p for p in self.passages if len(p)>0]
        return

    def issueN(self, n):
        issue = self.passages[n]
        assert(issue[0][0:5] == "Issue")
        paragraphs = []
        for i in range(1,len(issue)):
            if issue[i][-1] == '"' and issue[i][0] == '"':
                assert(i == 1)
                paragraphs.append(issue[i])
            elif issue[i][0] == '"':
                # assert(i == 1)
                if i==1:
                    paragraphs.append(issue[i])
                elif issue[i][1].isupper():
                    paragraphs.append('\n')
                    paragraphs.append(issue[i])
                elif issue[i][1].islower():
                    paragraphs[-1] += ' ' + issue[i]
                else:
                    assert(False)
            elif issue[i][-1] == '"':
                assert(i > 1)
                paragraphs[0] += ' ' + issue[i]
            elif issue[i][0].isupper():
                paragraphs.append('\n')
                paragraphs.append(issue[i])
            elif issue[i][0].islower():
                paragraphs[-1] += ' ' + issue[i]
            else:
                assert(False)
        parsed = [paragraphs[0].replace('"','')]
        for i in range(1,len(paragraphs)):
            if paragraphs[i] == '\n':
                parsed.append('\n')
            else:
                print(i)
                for temp in paragraphs[i].split(sep='. '):
                    if len(temp)>0:
                        parsed.append(temp + '.')
        out = open(self.outpath + 'issue' + str(n+12).zfill(3) + '.tex', 'w')
        out.writelines('\section{Issue '+ str(n+12) +'}\n')
        out.writelines('\paragraph{\n')
        out.writelines(parsed[0] + '\n' + '}\n')
        out.writelines('\subsection{Score 6}\n')
        for i in range(1,len(parsed)):
            out.writelines(parsed[i].replace('..', '.') + '\n')
        out.close()
        return


if __name__ == "__main__":
    w = writing("./workspace/issue.txt","./Issue/")
    for i in range(8, 123):
        w.issueN(i)