#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
class MainHandler(webapp2.RequestHandler):
    def getYourFortune(self):
        fortune = ["A man's work is from sun to sun, but a mother's work is never done",
        "A book is in your future.",
        "A friend asks only for your time not your money.",
        "A journey of 1000 miles begins with one step",
        "A long life may not be good enough, but a good life is long enough"
        ]
        display=random.choice(fortune)
        return display
    def get(self):
        luck=self.getYourFortune()
        content= "<h1> FORTUNE OF THE DAY</h1>"
        content+="<p>"+luck+"</P>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
