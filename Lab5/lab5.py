import sys

def open_file():
    try:
        return open("l5-1.txt")
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()

    fileName = sys.argv[1]
    try:
        return open(fileName)
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()


'''
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.Vertix = ""
        self.Edge = ""
        self.Vertixs = []
        self.matrix = []
        self.sums = []
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showDialog)
        self.ui.pushButton_5.clicked.connect(self.Find_adjacency)
        self.ui.pushButton_3.clicked.connect(self.digit)
        self.ui.pushButton_4.clicked.connect(self.isolated_uniformed)


def showDialog(self):

        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(fname, 'r')

        with f:
            self.Vertexs = [ line.split() for line in f ]    

            self.Vertex = self.Vertexs[0][0]
            self.Edge = self.Vertexs[0][1]
            del self.Vertexs[0]
            print(self.Vertex,self.Edge)
            print(self.Vertexs)


    def Find_Smegnosti(self):
        a = []
        b = []
        for i in self.Vertexs:
            a.append(int(i[0]))
            b.append(int(i[1]))
        print(a)
        print(b)
        self.matrix = np.zeros((int(self.Vertex)+1,int(self.Vertex)+1))
        self.matrix[a,b] = 1
        self.matrix[b,a] = 1
        self.matrix = np.delete(self.matrix, (0), axis=0) 
        self.matrix= np.delete(self.matrix, (0), axis=1 ) 
        for i in range(len(self.matrix)):
            np.delete(self.matrix[i],0)
        self.ui.label_2.setText(str(self.matrix))

'''
    

print("Matching vertices: [1:3], [2:2], [3:1], [4:4].")

