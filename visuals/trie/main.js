const fs = require("fs");

function node(name,par){
	par = par ? par : null;
	this.name = name;
	this._children = Object.create(null);
	this.parent = par;
}

function insert(pnode,word){
	if(word.length == 0)return;
	if(!(word[0] in pnode._children)){
		pnode._children[word[0]] = new node(word[0],pnode.name);
	}
	insert(pnode._children[word[0]],word.slice(1));
}

var contents = fs.readFileSync("../../data/SMSSpamCollection")
.toString()
.split("\n")
.map(i=>i.split("\t"))
.map(i=>i.slice(1).join(" "))
.map(i=>i.split(" "))
.reduce(function(x,y){
	Array.prototype.push.apply(x,y);
	return x;
})

var root = new node("root");

contents.forEach(i=>insert(root,i));

function replace__children(n){
	n._children = Object.keys(n._children).map(i=>n._children[i]);
	n._children.forEach(replace__children);
}

replace__children(root);
fs.writeFileSync("data.json",JSON.stringify(root));
