
import os
from website_writer import WebsiteWriter

home = os.environ.get('HOME')
print "Home: ", home

writer = WebsiteWriter("src/", home + "/public_html/", "boilerplate/_header.html", "boilerplate/_footer.html",
                       "Jordan Boyd-Graber", "http://umiacs.umd.edu/~jbg/")
writer.add_index("pubs/", "Publications", [("Year", 0, []), ("Category", 0, []), ("Authors", 1, ["Jordan Boyd-Graber"]), ("Venue", 0, [])])
writer.write()

writer.write_index("Publications", True)
