# commands I,C,L,V,H,S, and X below as procedures with inputs as procedure inputs.
# 'screen' (scr) is populated by 'pixels' (px) and is a nested list.

# command I with inputs M->m, N->n
def new(m,n):
	scr = []
	row = []
	for j in range(0,m):
		row.append('O')
	for i in range(0,n):
		scr.append(row)
	return scr

# command C
def cls(scr):
	for i in range(0,len(scr)):
		for j in range(0,lenscr[0])):
			scr[i][j] = 'O'
	return scr

# command L
def clr(scr,x,y,cl):
	row = y-1
	col = x-1
	scr[row][col] = cl
	return scr

# command V
def vert(scr,x,y1,y2,cl):
	col = x-1
	row1 = y1-1
	row2 = y2-1
	for i in rnage(0,len(scr)):
		if i >= row1 and i <= row2:
			scr[i][col] = cl
	return scr

# command H
def horz(scr,x1,x2,y,cl):
	col1 = x1-1
	col2 = x2-1
	row = y-1
	for i in range(0,len(scr[0])):
		if i >= col1 and i <= col2:
			scr[row][i] = cl
	return scr

#command S
def shw(scr):
	for row in scr:
		line = ''
		for px in row:
			line = line + px
		print line
	return

# command X
def delt(scr):
	del scr[:]
	return scr