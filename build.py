print('this is the build')

def main():
	top = ('templates/top.html')
	bottom = ('templates/bottom.html')
	blog = ('content/blog.html')
	testimonials = ('content/testimonials.html')
	index = ('content/index.html')

#combine top.html with bottom.htm ito base.html with {{content}}
	
	top_template = open(top).read()
	bottom_template = open(bottom).read()
	base_template = top_template + "{{content}}" + bottom_template
	#base_template = open('templates/base.html').read()
	open('templates/base.html', 'w+').write(base_template)


if __name__ == "__main__":
  main()

template = open('templates/base.html').read() 


def listdic():

	pages = [ {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Allsprout",
		}, 
		{
		"filename": "content/testimonials.html",
		"output": "docs/testimonials.html",
		"title": "Testimonials",
		}, 
		{
		"filename": "content/blog.html",
		"output": "docs/blog.html",
		"title": "Allsprout Blog",
		}
		]


	for page in pages:
		template = open('templates/base.html').read()
		filename = open(page['filename']).read()
		combined_file = template.replace("{{content}}",filename)
		open(page['output'],'w+').write(combined_file)

listdic()



def apply_template():


	#create and combine index html 
	template = open("templates/base.html").read()
	index_content = open("content/index.html").read()
	finished_index_page = template.replace("{{content}}", index_content)
	open("docs/index.html", 'w+').write(finished_index_page)


	return

apply_template()





#---------------------------------

#testimonial 
# content = open('content/testimonials.html').read()
# testimonials = top_template + content + bottom_template
# open('docs/testimonials.html', 'w+').write(testimonials) 


#blog
# content = open('content/blog.html').read()
# testimonials = top_template + content + bottom 

# #blog 
# page = open('content/blog.html').read()
# blog = top_template + page + bottom_template
# open('docs/blog.html', 'w+').write(blog) 

# #blog
# page = open('content/blog.html').read()
# blog = top_template + page + bottom_template
# open('docs/blog.html', 'w+').write(blog) 

# #blog
# #testimonial 
# page = open('content/blog.html').read()
# blog = top_template + page + bottom_template
# open('docs/blog.html', 'w+').write(blog) 



