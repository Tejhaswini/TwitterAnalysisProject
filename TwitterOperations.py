import string
import operator
import sys
def Operations():
    input_file = input("Enter the file path: ")
    input_file_path = input_file+ '.txt'
    with open (input_file_path, encoding = "latin-1") as mydataFile:
        twit = mydataFile.readlines()
    a = {}
    for dat in twit:
        fTmp = dat.split()
        if fTmp[0] in a:
            a[fTmp[0]] +=1
        else:
            a[fTmp[0]] = 1
    a = sorted(a.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open('C:/Users/tejua/Downloads/MaximumUsers.txt', 'w', encoding = "utf-8")
    outputFile.write(" : \n")
    for i in range (0,10):
        outputFile.write("The user " + a[i][0] + " tweeted " + str(a[i][1]) + " times" + "\n\n")   
    outputFile.close
    a1 = {}
    for dat in twit:
        fTmp = dat.split()
        fTmp1 = fTmp[1].split(":")
        twitterTmp = fTmp[0] + " " + fTmp1[1]
        if twitterTmp in a:
            a1[twitterTmp]+=1
        else:
            a1[twitterTmp]=1
    a1 = sorted(a1.items(), key = operator.itemgetter(1), reverse = True)
    a2 = {}
    totalNumPostsInFile = 0
    for dat in a1:
        totalNumPostsInFile+=1
        if(dat[0].split()[1]) in a2:
            a2[dat[0].split()[1]]+=1
    else:
            a2[dat[0].split()[1]]=1
    a2 = sorted(a2.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = 10*len(a2)
    outputFile = open('C:/Users/tejua/Downloads/MostUsersEveryHour.txt', 'w', encoding = 'utf-8')
    for x in range (0,len(a2)):
   
        mSearch = 10 
        for dat in a1:
            if mSearch == 0:
                break
            if dat[0].split()[1] == a2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n Hour: " + a2[x][0] +"\n")
                mSearch-=1
    outputFile.close
    a3 = {}
    for dat in twit:
        fTemp = dat.split()
        if fTemp[0] not in a:
            a3[fTemp[0]] = int(fTemp[-2])

    a3 = sorted(a3.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open('C:/Users/tejua/Downloads/MaxFollowers.txt', 'w', encoding = "utf-8")
    outputFile.write("The top 10 users who have the maximum followers: " + "\n\n\n")

    for i in range (0, 10):
        outputFile.write(str(i+1) + ". UserName: " + a3[i][0] + " - Number of followers are: " + str(a3[i][1]) + "\n\n\n")
    outputFile.close

    a4 = {}
    for dat in twit:
  
        fTmp = dat.split()
        y = len(fTmp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += fTmp[x] + " "
        tweet += " ::::;:::: " + fTmp[0]
        if tweet not in a:
            a4[tweet] = int(fTmp[-1])

    outputFile = open('C:/Users/tejua/Downloads/MaxRetweets.txt', 'w', encoding = "utf-8")
    a4 = sorted(a4.items(), key = operator.itemgetter(1), reverse = True)
    outputFile.write("The top 10 tweets who has the max number of retweets : " +"\n\n\n")

    for x in range (0,10):
        outputFile.write(str(x+1) + ". Username: " + a4[x][0].split()[-1] + "\n Tweet: " +
                      a4[x][0].split("::::;::::")[0] + "\n Number of retweets: " + str(a4[x][1]) + "\n\n\n")
    outputFile.close
Operations()
