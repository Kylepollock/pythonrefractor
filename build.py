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
	# open('template/base.html', 'w+').write(base_template)


if __name__ == "__main__":
  main()

# template = open('template/base.html').read() 


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
		# template = open('template/base.html').read()
		filename = open(page['filename']).read()
		# combined_file = template.replace("{{content}}",filename)
		# open(page['output'],'w+').write(combined_file)

listdic()

#create and combine index html 
# index_content = open(index).read()
# finished_index_page = template.replace("{{content}}", index_content)
# open('docs.html', 'w+').write(finished_index_page)


##testimonial 
# content = open('content/testimonials.html').read()
# testimonials = top_template + content + bottom_template
# open('docs/testimonials.html', 'w+').write(testimonials) 



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



