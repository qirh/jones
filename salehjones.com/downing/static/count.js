
//locations
var refc = ["Canada", "Great Britain", "Greece", "United States", "Mexico", "Germany", "Taiwan", "Germany", "Germany", "Hong Kong", "France"];
//currencies
var refu = ["CAD", "GBp", "EUR", "USD", "MXN", "TWD", "HKD"];
//exchanges
var refe = ["TOR", "LSE", "ASE", "NMS", "MEX", "FRA", "TAI", "BER", "MUN", "HKG", "PAR"];


//function will take an input and set it's href
function count(str, classn, k, href, id){
	var id = id + str;
	if(classn[0]+classn[1] == "co")
		var ref = refc;
	else if(classn[0]+classn[1] == "cu")
		var ref = refu;
	else
		var ref = refe;

	if(str.includes(",")){
		var tmp = str.split(",");
		for(i = 0; i < tmp.length; i++){

			tmp[i] = ref.indexOf(trim(tmp[i])) + 1;
		}

		var orig = document.getElementById(id);
		document.getElementById(id).innerHTML = trim(str.split(",")[0]);
		document.getElementById(id).href = href + tmp[0];

		for(i = 1; i < tmp.length; i++){
			var div = document.createElement('a');
			div.id = "cr " + str.split(",")[i];
			div.className = classn + k;
			div.textContent = trim(", " + trim(str.split(",")[i]));
			div.href = href + tmp[i];
			orig.appendChild(div);
		}
	}
	else{
		var orig = document.getElementById(id);
		//console.log("'" + id + "'");
		document.getElementById(id).innerHTML = str;
		var num = ref.indexOf(str) + 1;
		document.getElementById(id).href = href + num;
	}
	return true;
}

/* for duplicate cells (same text value)	*/
function change_links(str, classn, k, href, id){
	
	for (var elems = [], i = document.getElementsByClassName(classn + k).length - 1; i > -1; --i){
		elems[i] = document.getElementsByClassName(classn + k)[i];
	}
	var tmp = [];
	for(var i = 0; i < elems.length; i++)
		if(trim(str) == trim(elems[i].innerHTML))
			tmp.push(elems[i]);

	for (var i = 1; i<tmp.length; i++){
		//console.log(tmp[i])
		tmp[i].href = tmp[0].href;
	}
	
	return true;
}
function count_helper(classn, k, href, id, change_link, b){
	b = b || 0;
	//print(b);
	//converts nodelist to array
	for (var elems = [], i = document.getElementsByClassName(classn + k).length - 1; i > -1; --i){
		elems[i] = document.getElementsByClassName(classn + k)[i];
		//console.log("TMP " + elems[i].textContent)
	}

	var repeated = [];
	for(i = 0; i < elems.length; i++){

		if (repeated.indexOf(elems[i].textContent) == -1){
			//console.log("NOT REPEATED " + elems[i].textContent)
			count(trim(elems[i].textContent), classn, k, href, id);
			if(change_link)
				change_links(trim(elems[i].textContent), classn, k, href, id);
			repeated.push(elems[i].textContent);
		}
		else{
			//console.log("REPEATED " + elems[i].textContent)
		}
	}	
}
/*	trim will remove trailing and starting white space	*/
function trim(s){ 
	return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}
/*	only for testing purposes, will print to the console	*/
function print(b){ 
	console.log(" ----- PRINT ---- " + b);
}