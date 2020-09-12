# Inporting required modules
import requests
import json
import jsonpath

def test_postRequest():
    #print('**********Storing req. end point in variable **********')
    url = 'https://reqres.in/api/users'
    #print('**********Fetching the file in read mode & storing in a variable**********')
    v_fileContent=open('C:\\RestPythonTestFiles\\postJson.json',mode='r')
    print(v_fileContent)
    #print('**********Reading contents of the file from variable using read() function**********')
    v_fileJSON=v_fileContent.read()
    print(v_fileJSON)
    #print('**********Triggering the POST/ create request**********')
    v_resp=requests.post(url,v_fileJSON)
    print(v_resp)
    #print('**********Response Status code**********')
    v_status=v_resp.status_code
    print(v_status)
    #print('**********Obtaining the text from response using .text property**********')
    v_respContent=v_resp.text
    print(type(v_respContent))
    #print('*********Coverting string Response text obtained to JSON format for reading it by JSON parsing**********')
    v_respJson=json.loads(v_respContent)
    print(v_respJson)
    #print('*********Retrieving id value using jsonpath parsing**********')
    respId=jsonpath.jsonpath(v_respJson,'id')
    print(respId)
    #print('*********Validating status code through assertion**********')
    assert v_status==201

def test_putRequest():
    url = 'https://reqres.in/api/users/2'
    v_filecontent = open('C:\\RestPythonTestFiles\\putJson.json', mode='r')
    v_filecontent = v_filecontent.read()
    v_fileJson = json.loads(v_filecontent)
    print(v_fileJson)
    print(v_fileJson['name'])
    jsonpath.jsonpath(v_fileJson, 'name')
    v_resp = requests.put(url, v_fileJson)
    print(v_resp)
    v_resptext = v_resp.text
    type(v_resptext)
    v_respJson = json.loads(v_resptext)
    print(v_respJson)
    v_respname = jsonpath.jsonpath(v_respJson, 'name')
    v_respdate = jsonpath.jsonpath(v_respJson, 'updatedAt')
    assert v_respname[0] == v_fileJson['name']
    assert v_resp.status_code == 200
    assert v_respdate is not None