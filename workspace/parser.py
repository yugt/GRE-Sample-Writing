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
        return issue


if __name__ == "__main__":
    w = writing("./workspace/issue.txt","")
    print(w.issueN(0))