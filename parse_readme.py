import pprint

fname = "README.md"
snipepts = []

with open(fname, 'r') as f:
	lines = f.readlines()
	for line in lines:
		# check if it's a H3
		if line.startswith("###"):
			title = line.replace("### ", "")
			# get Title, des
			# store lines till an H4 (explanation) is encountered
			# store lines again until --- or another H3 is encountered
			snippets.append({
					"title":,
					"description":,
					"explanation":
				})
			# repeat until EOL is encoutered

# separating by category
categories = ["a", "b", "c"]

snips_by_cat = {k:[] for k in categories}

for snip in snippets:
	cat = raw_input(snip["title"])
	snips_by_cat[cat].append(snip)

pprint.pprint(snips_by_cat)
