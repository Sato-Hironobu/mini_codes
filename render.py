def render(text, width, head_length):

	lpos = 0
	out_str = out_text = ""
	head_str = " " * head_length
	for ch in text:
		if ch == " ":
			lpos += len(out_str) + 1
			if lpos > width:
				out_text += "\n"
				out_text += head_str
				lpos = len(out_str) + 1
			out_text += out_str + ch
			out_str = ""
		else:
			out_str += ch
	if lpos + len(out_str) > width:
		out_text += "\n" 
		out_text += head_str
	out_text += out_str
	
	return out_text
