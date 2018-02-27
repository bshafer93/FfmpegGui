from PyQt4 import QtGui, QtCore
import sys
import os
import design
import re
import urllib,json,urllib2 
import random
import time


#Declare which version of ffmpeg you would like to use

config_file = open('config.json')    
config = json.load(config_file)
FFMPEG = config['linux']['ffmpeg_path']
apiK = config['giphy']['api_key']
searchArray = config['giphy']['search_list']
accepted_fileext = config['universal']['img_fileExt']
localGiph = config['giphy']['giph_path']
print localGiph


class offTransApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self) 
        #### TAB 1.###################################################################
        self.v1_t1_btn.clicked.connect(lambda: self.browse_file(self.v1_t1))
        self.v1_t1.textEdited.connect(lambda: self.clean_input(self.v1_t1))
        self.v1_t1.textChanged.connect(lambda: self.autoFill(self.v1_t1,self.o1_t1))
        self.o1_t1_btn.clicked.connect(lambda: self.browse_directory(self.o1_t1))
        self.transcode1_t1.clicked.connect(self.movie_toframes)
        #### TAB 1.###################################################################

        #### TAB 2.###################################################################
        self.v1_t2_btn.clicked.connect(lambda: self.browse_file(self.v1_t2))
        self.v1_t2.textEdited.connect(lambda: self.clean_input(self.v1_t2))
        self.v1_t2.textChanged.connect(lambda: self.autoFill(self.v1_t2,self.o1_t2))
        self.a1_t2_btn.clicked.connect(lambda: self.browse_file(self.a1_t2))
        self.a1_t2.textEdited.connect(lambda: self.clean_input(self.a1_t2))
        self.o1_t2_btn.clicked.connect(lambda: self.browse_directory(self.o1_t2))
        self.transcode1_t2.clicked.connect(self.merge_av)
        #### TAB 2.###################################################################

        #### TAB 3.###################################################################
        self.v1_t3_btn.clicked.connect(lambda: self.browse_file(self.v1_t3))
        self.v1_t3.textEdited.connect(lambda: self.clean_input(self.v1_t3))
        self.v1_t3.textChanged.connect(lambda: self.autoFill(self.v1_t3,self.o1_t3))
        self.o1_t3_btn.clicked.connect(lambda: self.browse_directory(self.o1_t3))
        self.remove1_t3.clicked.connect(self.remove_audio)
        #### TAB 3.###################################################################

        #### TAB 4.###################################################################
        self.v1_t4_btn.clicked.connect(lambda: self.browse_file(self.v1_t4))
        self.v1_t4.textEdited.connect(lambda: self.clean_input(self.v1_t4))
        self.v1_t4.textChanged.connect(lambda: self.autoFill(self.v1_t4,self.o1_t4))
        self.o1_t4_btn.clicked.connect(lambda: self.save_file(self.o1_t4))
        self.extract_t4.clicked.connect(self.extract_audio)
        #### TAB 4.###################################################################

        #### TAB 5.###################################################################
        self.v1_t5_btn.clicked.connect(lambda: self.browse_file(self.v1_t5))
        self.v1_t5.textEdited.connect(lambda: self.clean_input(self.v1_t5))
        self.v1_t5.textChanged.connect(lambda: self.autoFill(self.v1_t5,self.o1_t5))
        self.a1_t5_btn.clicked.connect(lambda: self.browse_file(self.a1_t5))
        self.a1_t5.textEdited.connect(lambda: self.clean_input(self.a1_t5))
        self.o1_t5_btn.clicked.connect(lambda: self.save_file(self.o1_t5))
        self.transcode1_t5_btn.clicked.connect(self.combine_imgandaudio)
        #### TAB 5.###################################################################


    def autoFill(self,ipath,opath):
        namesDict = self.deduce_names(ipath.text())

        if opath == None: 
            pass

        if self.tabOptions.currentIndex() == 0:
                newDir = namesDict['fullFolderPath']
                if self.mkdir_t1.isChecked():
                    

                    if not os.path.exists(newDir):
                        os.makedirs(unicode(newDir))
                        print("New directory made")  
                opath.setText(newDir)

        elif self.tabOptions.currentIndex() == 1:
            opath.setText(namesDict['basicPath'] + namesDict['baseFileName'] + "_WITH_AUDIO" + namesDict['fileExt'] ) 

        elif self.tabOptions.currentIndex() == 2:
            opath.setText(namesDict['basicPath'] + namesDict['baseFileName'] + ".wav")

        elif self.tabOptions.currentIndex() == 3:
            buildName = namesDict['basicPath'] + namesDict['baseFileName'] + "_NO_AUDIO" + namesDict['fileExt']
            opath.setText(buildName )

        elif self.tabOptions.currentIndex() == 4:
            opath.setText(namesDict['basicPath'] + namesDict['baseFileName'] + "mov" )
            indexNum = len(namesDict['frameNumber']) -1 
            self.pad1_t5.setCurrentIndex(indexNum)
            self.sf1_t5.setText(namesDict['frameNumber'])

    def clean_input(self,ipath):
        video1 = ipath.text()
        replaced = video1.replace("file://","")
        NoSpace = replaced.replace("%20"," ")
        cleanedInput = NoSpace.trimmed()
        

        ipath.setText(cleanedInput)
        print(cleanedInput)

    def make_gif(self):
        start_time = time.time()
        searchTerm = searchArray[random.randint(0,len(searchArray))]
        randnum = random.randint(0,20)
        searchBuild = "http://api.giphy.com/v1/gifs/search?q={0}&api_key={1}&limit=20&rating=G&lang=en".format(searchTerm,apiK)
        

        data = json.loads(urllib.urlopen(searchBuild).read())
        giph = data['data'][randnum]['images']['downsized_medium']['url']

        getGiph = urllib2.urlopen(giph)
        dGiph = getGiph.read()
        binfile = open(localGiph, "wb")
        binfile.write(dGiph)
        binfile.close()

        et2 = time.time() - start_time
        print "Time to Download: "+ str(et2)
        self.movie = QtGui.QMovie(localGiph,QtCore.QByteArray(),self)
        size = self.movie.scaledSize()
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.mo1_t5.setMovie(self.movie)
        self.movie.start()
        elapsed_time = time.time() - start_time

        print "Final: "+ str(elapsed_time)

    def deduce_names(self,filePath):

        r = re.match(r'(.*\/)([^\/]*)([.].*)',filePath)
        fileExt = r.group(3)

            
        if fileExt in accepted_fileext:
            r = re.match(r'(.*\/)([^\/]*[.])(\d*)([.].*)',filePath)
            baseFileName = r.group(2)
            basicPath = r.group(1)
            frameNumber = r.group(3)
            fileExt = r.group(4)
            fullFolderPath = basicPath + baseFileName
            return {'wavName': None,'baseFileName': baseFileName,'fullFolderPath':fullFolderPath,'basicPath': basicPath ,'fileExt': fileExt,'frameNumber': frameNumber}

        else: 
            baseFileName = r.group(2)
            basicPath = r.group(1)
            fileExt = r.group(3)
            fullFolderPath = basicPath + baseFileName
            wavName = fullFolderPath +"/"+ baseFileName + ".wav"

            return {'wavName':wavName,'baseFileName' :baseFileName,'fullFolderPath' :fullFolderPath,'basicPath' :basicPath,'fileExt': fileExt} 

    def save_file(self,opath):
        file = QtGui.QFileDialog.getSaveFileName(self,"Save a file")
        opath.setText(file)
                
    def browse_directory(self,path):
        directory =  QtGui.QFileDialog.getExistingDirectory(self,"Pick A Directory")
        if directory:
            path.setText(directory)
            ####

    def movie_toframes(self):

        file = self.v1_t1.text()
        fps = self.fps1_t1.currentText()

        namesDict = self.deduce_names(file)

        jpgName = namesDict['fullFolderPath'] +"/"+ namesDict['baseFileName']
        print jpgName
        print file


        if self.cb1_t1.isChecked():
            ffmpegCmd = '\"'+FFMPEG+'\"' +" -i \"{0}\"-q:a 0 -map 0:a? \"{1}\" -map 0:v -q:v 2 -r {3} \"{2}.%04d.jpg\"".format(file,namesDict['wavName'],jpgName,fps)
        else:
            ffmpegCmd = '\"'+FFMPEG+'\"' +" -i \"{file}\"  -r {fps} -q:v 2 \"{jpgName}.%04d.jpg\"".format(file = file, jpgName=jpgName ,fps=fps)
            print ffmpegCmd

        
        
 
        done = os.system(ffmpegCmd)

        if done == 0:
            choice = QtGui.QMessageBox.information(self,"Success!","Offline Transcode Successfull!")

   
    def merge_av(self):
        video1 = self.v1_t2.text()
        audio1 = self.a1_t2.text()
        output1 = self.o1_t2.text()

        
        ffmpegCmd = '\"'+FFMPEG+'\"' +" -i \"{0}\" -i \"{1}\" -c copy -map 0:0 -map 1:0 -c:a aac \"{2}\"".format(video1,audio1,output1)

        done = os.system(ffmpegCmd)

        if done == 0:
            choice = QtGui.QMessageBox.information(self,"Success!","Audio Added") 

    def remove_audio(self):
        video1 = self.v1_t3.text()
        output1 = self.o1_t3.text()
        #ffmpeg -i {input} -codec copy -an {output}  
        ffmpegCmd = '\"'+FFMPEG+'\"' +" -i \"{0}\" -codec copy -an \"{1}\"".format(video1,output1)

        done = os.system(ffmpegCmd)

        if done == 0:
            choice = QtGui.QMessageBox.information(self,"Success!","Audio Removed!") 
    
    def combine_imgandaudio(self):
        self.make_gif()
        video1 = self.v1_t5.text()
        audio1 = self.a1_t5.text()
        startFrame = self.sf1_t5.text()
        output1 = self.o1_t5.text()
        fps = self.fps1_t5.currentText()
        numPadding = self.pad1_t5.currentText()

        namesDict = self.deduce_names(video1)


        #ffmpeg -start_number  {theStartFrame} -framerate 23.976 -i {input}.%04d.{ext}  -i {input}.wav  -codec:v prores -profile:v 2 -r 59.94 -shortest -strict -2 -c:v copy {output}.mov 
       
        ffmpegCmd = '\"'+FFMPEG+'\"' +" -start_number {startFrame} -framerate {fps} -i \"{basicPath}{baseFileName}{numPad}{fileExt}\"  -i \"{audio}\"  -c:v prores -profile:v 3 -r {fps} -shortest -strict -2 -acodec pcm_s32le \"{output}\"".format(startFrame = namesDict['frameNumber'],fps = fps, baseFileName = namesDict['baseFileName'],audio = audio1, numPad = numPadding, fileExt = namesDict['fileExt'],output = output1,basicPath = namesDict['basicPath'] )
        print ffmpegCmd
        done = os.system(ffmpegCmd)

        if done == 0:
            choice = QtGui.QMessageBox.information(self,"Success!","Prores has been made!") 

    def extract_audio(self):
        video1 = self.v1_t4.text()

        if self.o1_t4.text() == "":

            namesDict = self.deduce_names(video1)
            output1 = namesDict['wavName']
            o1_t4.setText(namesDict['wavName'])
        else:
            output1 = self.o1_t4.text()
            print(output1)



        #ffmpeg -i my_video.mp4 -vn -acodec wav output_audio.wav
        ffmpegCmd = '\"'+FFMPEG+'\"' +" -i \"{0}\" -vn -acodec pcm_s32le \"{1}\"".format(video1,output1)

        done = os.system(ffmpegCmd)

        if done == 0:
            choice = QtGui.QMessageBox.information(self,"Success!","Audio Extracted!") 

    def browse_file(self,vpath):

        file = QtGui.QFileDialog.getOpenFileName(self,"Pick A File")
        vpath.setText(file)


def main():
    app = QtGui.QApplication(sys.argv)  
    form = offTransApp()                 
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              
    main()                              





