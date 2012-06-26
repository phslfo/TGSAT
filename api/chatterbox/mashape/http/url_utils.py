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

from mashape.config.module_info import ModuleInfo

import re
import urllib

class UrlUtils:
	
	@staticmethod
	def remove_query_string(url):
		return url.split("?")[0]

	@staticmethod
	def get_query_string_parameters(query):
		result = {}
		if len(query) > 0:
			for param in query.split("&"):
				keyValue = param.split("=")
				if(len(keyValue) > 1):
					if (not UrlUtils.is_placeholder(keyValue[1])):
						result[keyValue[0]]=keyValue[1]
		return result

	@staticmethod
	def is_placeholder(val):
		return re.match('\{([a-zA-Z0-9_\\.]*)\}', val)
		
	@staticmethod
	def replace_base_url_parameters(url, parameters):
		final_url = url
		keys = re.findall('\{([a-zA-Z0-9_\\.]*)\}', final_url)
		for key in keys:
			if key in parameters:
				final_url = re.sub("\{"+key+"\}&?", urllib.quote_plus(parameters[key]), final_url)
				parameters.pop(key)
		return final_url
	
	@staticmethod
	def generate_client_headers():
		return {"X-Mashape-Language": ModuleInfo.CLIENT_LIBRARY_LANGUAGE, "X-Mashape-Version" : ModuleInfo.CLIENT_LIBRARY_VERSION}
