

# Load the AlchemyAPI module code.
import AlchemyAPI

# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt")


# Extract a ranked list of named entities from a text string, using the supplied parameters object.
result = alchemyObj.TextGetTargetedSentiment("Madonna enjoys tasty Pepsi.  I hate Madonna style.", "Pepsi");
print result


