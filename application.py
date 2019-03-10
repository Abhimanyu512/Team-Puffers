from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.tokeize import word_tokenize
from nltk.stem import PortStemmer,WordNetLemmatizer

app = Flask(__name__)
@app.route("/")
def index(method=["POST"]):
    business_name = request.form.get("business_name")
    business_type = request.form.get("business_type")
    description = request.form.get("description")
def DataPreProcess():
	token=word_tokenize(description)
	stop_words=set(stopwords.words('english'))
	result=[i for i in tokens if not i in stop_words]
stemmer=PortStemmer()
for word in description:
	result1=[stemmer.stem(word)]
lemmatizer=WordNetLemmatize()
for word in description:
	result2=[lemmatizer.lemmatize(word)]
#description would be asked in flask
#business tpe would be asked in drop down menu

def NameSuggestor():
	business_description=description
	processed_business_description=result 	#description after processing
	stemmed_business_description=result2
	domainNameSuggestions=[]
	business_type=business_type.split(' ')
	if len(business_type>1):
		#create a new field where the user has to input the main function of the product
		mainFunction=input('Enter the main function of your product: ')
		domainNameSuggestions.append(mainFunction)
		#Implement a search whether the name has already been taken or not
		#Use an API to check this (GoDaddy)
def DomainNameGenerator():
	DomainNames=[]
	for j in range(0,len(domainNameSuggestions)):
		dnx='.com'.join(DomainNamesSuggestions[i])
		DomainNames.append(dn)
	for k in range(0,len(processed_business_description):
		dnx1='.com'.join(processed_business_description[i])
		DomainNames.append(dn1)
	for h in range(0,len(stemmed_business_description)):
		dnx2='.com'.join(stemmed_business_description[i])
		DomainNames.append(dn2)
	#Ask the user of he/she wants the domain names with different extensions other than .com
	q=input('Do you want domain names with other extensions (other than .com)[Y/N]? ')
	q=q.lower()
	if q=='y':
		for j in range(0,len(domainNameSuggestions)):
			dn=[['.in'.join(DomainNamesSuggestions[j])],['.org'.join(DomainNameSuggestions[j])]]
		for k in range(0,len(processed_business_description)): 
			dn1=[['.in'.join(processed_business_description[k])],['.org'.join(stemmed_business_description[k])]]
		for h in range(0,len(stemmed_business_description):
			dn2=[[.'.in'.join(stemmed_business_description[h]],[.'.org'.join(stemmed_businedd_description[h])]]
	for i in range(0,len(domainNameSuggestions)):
		for j in range(0,len(domainNameSuggestions)):
			DomainNames.append(dnx[i][j])
	for i in range(0,len(processed_business_description)):
		for j in range(0,len(processed_business_description)):
			DomainNames.append(dnx1[i][j])
	for i in range(0,len(stemmed_business_description)):
		for j in range(0,len(stemmed_business_description)):
			DomainNames.append(dnx2[i][j])
return render_template("main.html",business_name=business_name,business_type=business_type,description=description)

