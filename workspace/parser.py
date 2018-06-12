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

    def issue(self):
        temp = []
        for line in self.lines:
            if line[0:5] == "Issue":
                self.empty_line = False
                temp.append(line)
            elif line[0] == '\n' or line == '':
                if ~self.empty_line:
                    self.empty_line = True
                    self.passages.append(temp)
                    temp = []
            else:
                temp.append(line)
        self.passages = filter(lambda x: len(x)>0, self.passages)
        return self.passages

if __name__ == "__main__":
    w = writing("./workspace/issue.txt","")
    print(w.issue())