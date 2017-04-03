function getTline(v,flag=0){
	var tmp="";
	var i=0;
	tmp +='<tr>';
	
	for(p in v){
		if((flag==0&&i==0)||(flag!=0)){//first column or first column
			th='<th>';
			thr='</th>';
		}
		else{
			th='<td>';
			thr='</td>';
		}
		tmp +=th;
		if(flag==1){tmp +=p;}
		else{
        	if(v[p]==null) tmp +='*';//NA	
			else tmp +=v[p];
		}
		tmp +=thr;
		i = i+1;
	}
	tmp +='</tr>';
	return tmp;
}
$(document).ready(function(){
	$('#btnsubmit').click(function(){
	var value=$("#factor option:selected").val();
	var select={"select":value};

	$.ajax({
		type:'POST',
		url:'/dashboard',
		data:select,
		success:function(data){
			//alert("receive data success!");
			table="";
			$.each(data,function(k,v){
				if(k=="0"){//first row
					table += getTline(v,1);
					table += getTline(v);
				}
				else
					table +=getTline(v);				
			});
			$('#Result').html(table);
		},
		dataType:'json'
		});
	return false;
	});
});
