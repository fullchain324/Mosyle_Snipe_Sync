import base64
import requests
import jwt
import time

class Mosyle:
	
	# Create Mosyle instance
	def __init__(self, key="access_token", url = "https://businessapi.mosyle.com/v1", jwt_secret = "jwt_secret"):
		# Attribute the variable to the instance
		self.url = url
		self.request = requests.Session()
		self.jwt_secret = jwt_secret

		# Generate a JWT token
		payload = {
            "iss": "your_issuer",
            "sub": "your_subject",
            "exp": int(time.time()) + 3600  # Token expires in 1 hour
        }
		self.jwt_token = jwt.encode(payload, self.jwt_secret, algorithm="HS256")
		print(self.jwt_token)
	    # Set the JWT token in the request headers
		self.request.headers = {
			"Authorization": f"Bearer {self.jwt_token}",
			"Content-Type": "application/json",
			"accessToken": self.jwt_token
		}
		
	# Create variables requests
	def list(self, os):
		print("Listing devices for OS:", os)
		params = {
			"operation": "list",
			"options": {
				"os": os
			}
		}
		# Concatanate url and send the request
		return self.request.post(self.url + "/devices", json = params )

	def listTimestamp(self, start, end, os):
		params = {
			"operation": "list",
			"options": {
				"os": os,
				"enrolldate_start": start,
				"enrolldate_end": end	
			}
		}
		return self.request.post(self.url + "/devices", json = params )

	def listmobile(self):
		params = {
			"operation": "list",
			"options": {
				"os": "ios"
			}
		}
		return self.request.post(self.url + "/devices", json = params )

	def listuser(self, iduser):
		params = {
			"operation": "list_users",
			"options": { "identifiers": [iduser]
				}
		}
		return self.request.post(self.url + "/users", json = params )
    
	def setAssetTag(self, serialnumber, tag):
		params = {
			"operation": "update_device",
			"serialnumber": serialnumber,
			"asset_tag": tag
		}
		return self.request.post(self.url + "/devices", json = params )