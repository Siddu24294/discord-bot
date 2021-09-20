import time
import re
import requests
import random
#from googlesearch import search as gsearch
'''

def logger(log):
	f=open("log.txt","a+")
	f.write(log)
	f.flush()
	f.close()

'''


async def bthelp(ctx):
	f=open("help.txt","r")
	s="```"+f.read()+"```"
	await ctx.send(s)


def wallpaperList(searchTerm=''):
	query = "https://wallhaven.cc/search?q="
	query+=searchTerm
	print(searchTerm,query)
	list = requests.get(query).text
	return re.findall(r"(https://wallhaven.cc/wallpaper/tags/[a-zA-Z0-9]+)", list)



async def search(ctx,word,sentence):
	c=0
	for i in range(len(sentence)-len(word)):
		if sentence[i:i+len(word)]==word:c+=1;await ctx.send(f"```{i}\t{sentence[i:i+len(word)]}```")
	await ctx.send(f"```total occurences of {word} in \n{sentence}\n are {c}```")


'''async def image(ctx,searchTerm):
	print(searchTerm)
	resultList=list(result for result in gsearch(searchTerm,tld="co.in",num=5,stop=5,pause=30))
	for i in resultList:print(i);await ctx.send(i)'''


async def wallpaper(ctx,searchTerm,shortlist=0):
	wallsList=wallpaperList(searchTerm)
	if len(wallsList)==0:wallsList=[f"```No matches Found for {searchTerm}.\nPlease check spelling and try again.```"]
	if shortlist==0:shortlist=10
	if shortlist>len(wallsList):shortlist=len(wallsList)
	for i in wallsList[:shortlist]:await ctx.send(i)