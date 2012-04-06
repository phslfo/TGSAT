#
# Mashape Python Client library.
# Copyright (C) 2011 Mashape, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# The author of this software is Mashape, Inc.
# For any question or feedback please contact us at: support@mashape.com
#

import sys
sys.modules['ssl'] = None

import urllib
import urllib2
from libs import httplib2
import simplejson as json
import threading
from urlparse import urlparse
from libs.textprocessing.mashape.config.module_info import ModuleInfo 
from libs.textprocessing.mashape.http.url_utils import UrlUtils
from libs.textprocessing.mashape.http.auth_utils import AuthUtils
from libs.textprocessing.mashape.exception.client_exception import MashapeClientException

class HttpClient:
	def do_call(self, http_method, url, parameters, has_mashape_auth, public_key, private_key, callback=None, parse_json=True):
		if(callback != None):
			def thread_function(http_method, url, parameters, has_mashape_auth, public_key, private_key, parse_json):
				result = self._do_call(http_method, url, parameters, has_mashape_auth, public_key, private_key, parse_json)
				callback(result)
			thread = threading.Thread(target=thread_function, args=(http_method, url, parameters, has_mashape_auth, public_key, private_key, parse_json))
			thread.start()
			return thread
		else:
			return self._do_call(http_method, url, parameters, has_mashape_auth, public_key, private_key, parse_json)


	def _do_call(self, http_method, url, parameters, has_mashape_auth, public_key, private_key, parse_json):
		if parameters == None:
			parameters = {};
		else:
			for key in parameters.keys():
				if parameters[key] == None:
					parameters.pop(key)
		
		parsedUrl = urlparse(url)
		parameters.update(UrlUtils.get_query_string_parameters(parsedUrl.query))

		headers = {"Content-type": "application/x-www-form-urlencoded"}
		if parse_json:
			headers["Accept"] = "application/json"

		headers.update(UrlUtils.generate_client_headers())
		if has_mashape_auth:
			headers.update(AuthUtils.generate_authentication_header(public_key, private_key))
			
		# if you have SSL issues (invalid certificate), try:
		# h = httplib2.Http(disable_ssl_certificate_validation=True) 
		h = httplib2.Http()
		qpos = url.find("?")
		if ( qpos > 0 ):
			url = url[:qpos]
		url = UrlUtils.replace_base_url_parameters(url, parameters)

		params = urllib.urlencode(parameters)
		request = urllib2.Request(url, params, headers)
		if (http_method == "GET"):
			url += "?" + params
			request = urllib2.Request(url, None, headers)
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request.get_method = lambda: http_method
		try:
			responseValue = opener.open(request).read()
		except:
			import sys
			raise MashapeClientException("Error executing the request " + str(sys.exc_info()[1]), 2000)

		responseJson = None
		if responseValue != None and parse_json:
			responseJson = json.loads(unicode(responseValue, errors='replace'))
			return responseJson
		else:
			return responseValue
