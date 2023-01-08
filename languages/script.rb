require "uri"
require "net/http"

url = URI("http://127.0.0.1:5000/register")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Accept"] = "application/json"
form_data = [['username', '{username}'],['email', '{email}'],['password', '{password}'],['password_confirmation', '{password_confirmation}']]
request.set_form form_data, 'multipart/form-data'
response = http.request(request)
puts response.read_body