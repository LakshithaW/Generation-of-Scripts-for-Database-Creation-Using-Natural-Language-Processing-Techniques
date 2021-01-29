<!DOCTYPE html>
<html lang="en">
 
<?php 
include "digrams.php";
  
$command = "python ../ashan/nor.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 usleep(100000);
}
pclose($pid);

$command = "python ../ashan/sql.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 usleep(100000);
}
pclose($pid);
?>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<body>

<div class="row">
  <div class="col-sm-4"></div>
  <div class="col-sm-4"><h2>Select dependency</h2></div>
  <div class="col-sm-4"></div>
</div>
<?php 
        
				$studentid = $_SESSION['s_id'];
				$host="localhost";
				$user="root";
				$pass="";
				$con = @mysql_connect("$host","$user","$pass");
	

				if (!$con)
				  {

				echo "Error in DBConnect() = " . mssql_get_last_message();
				  die('Could not connect: ' . mysql_error());

				  }

				mysql_select_db("s2ecd", $con);
	
				$sql = "SELECT * from reg where id='{$studentid}'";
				$result = mysql_query($sql,$con);
				$row1=mysql_fetch_array($result);
                $user=$row1['username'];
?>

 <div class="row">
  <div class="col-sm-2"></div>
   <div class="col-sm-5">
    <h4>Select Table </h4>
    <select name="table" id="table"  style="width:230px;">
<?php
include('db.php');

$query = "SELECT * FROM test where u_name='{$user}'";
mysqli_query($db, $query) or die('Error querying database.');

    $result = mysqli_query($db, $query);
    $projects = array();


while ($row = mysqli_fetch_array($result)) {
        $projects[] = $row;
    }
    $i=0;
    foreach ($projects as $row)
    {
      //echo $row['name'];
    
?>
  <option value="<?php echo $row['id']; ?>"><?php echo $row['name']; ?></option>
    <?php } ?>
</select>
   <button type="button" class="btn btn-info" id="submit" style="padding: 4px 12px;">ok</button>
  </div>
</div> 
</br></br>

 <div class="row">
  <div class="col-sm-2"></div>
   <div class="col-sm-5">
      <select id="selectNumber" style="width:230px;">
         <option>choose a Dependency</option>
      </select>
      <button type="button" class="btn btn-info" id="submit2" onclick="myFunction()" style="padding: 4px 12px;">ok</button>
   </div>
   <div class="col-sm-5">
      <select id="selectNumber2"  style="width:230px;">
         <option>choose a Dependency</option>
      </select>
      <button type="button" class="btn btn-info" onclick="myFunction2()" id="submit3" style="padding: 4px 12px;">ok</button>
   </div>
 </div>
 </div>
</br></br><hr>
 <div class="row">
  <div class="col-sm-4"></div>
   <div class="col-sm-4">
   <h2>X - Independent</h2>
<table id="myTable" class="myTable">
</table>

</div>
  <div class="col-sm-4"></div>
<h2>Y - Dependent</h2>
<table id="myTable2" class="myTable2">
</table>
</div>
</br></br></br></br></br></br><hr>
<div style="text-align:center;">
  <a type="button" href="RDBMS.php" class="btn btn-info" onclick="myFunction3(),myFunction4()" id="submit4">Save</a> &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;
  <a type="button" href="RDBMS1.php" class="btn btn-info" onclick="" id="submit4">Ignore</a>
</div>
</br></br></br></br></br></br>
<script>
function postUserMessage() {

	var input = document.getElementById("table").value;
	var data = { uMsg: input};
    $("#selectNumber option").remove();
    $("#selectNumber2 option").remove();
    
	var request = new XMLHttpRequest();
	request.open("POST", "http://localhost/mysite/views/tt2.php");
	request.setRequestHeader("Content-Type", "application/json");
	request.overrideMimeType("text/plain");
	request.onload = function(response)
	{
        var data = request.responseText;
        var splitData = data.split(",");
        console.log(splitData);
        var select = document.getElementById("selectNumber");
        var options = splitData;
            for(var i = 0; i < options.length; i++) {
                var opt = options[i];
                var el = document.createElement("option");
                el.textContent = opt;
                el.value = opt;
                select.appendChild(el);
}
        var select = document.getElementById("selectNumber2");
        var options = splitData;
            for(var i = 0; i < options.length; i++) {
                var opt = options[i];
                var el = document.createElement("option");
                el.textContent = opt;
                el.value = opt;
                select.appendChild(el);
}
	};
	request.send(JSON.stringify(data));
}

document.addEventListener('DOMContentLoaded', function() {
	document.getElementById("submit").addEventListener("click", postUserMessage);
});

</script>


<script>
function myFunction() {
  	var input = document.getElementById("selectNumber").value;
    var input2 = document.getElementById("selectNumber2").value;
    var table = document.getElementById("myTable");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = input;
    //cell2.innerHTML = input2;
}
function myFunction2() {
  	var input = document.getElementById("selectNumber").value;
    var input2 = document.getElementById("selectNumber2").value;
    var table = document.getElementById("myTable2");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    //cell1.innerHTML = input;
    cell2.innerHTML = input2;
}
function myFunction3() {

var table = document.getElementsByTagName('table')[0];
//console.log(table);
var rows = table.rows;
//console.log(rows.length);
for (var i = 0; i < rows.length; i++) {
    var rowText = rows[i].textContent;
    //console.log(rowText);
}
}

function myFunction4() {

var table = document.getElementsByTagName('table')[1];
//console.log(table);
var rows = table.rows;
//console.log(rows.length);
for (var i = 0; i < rows.length; i++) {
    var rowText = rows[i].textContent;
    //console.log(rowText);
}
}

function postUser() {
	var lines = [];

    var table2 = document.getElementsByTagName('table')[0];
  var rows2 = table2.rows;
for (var i = 0; i < rows2.length; i++) {
    var rowText = rows2[i].textContent;
     lines.push(rows2[i].textContent);
    
   }
    //jjjjjjjjjjjjjj
  var table = document.getElementsByTagName('table')[1];
  var rows = table.rows;
for (var i = 0; i < rows.length; i++) {
    var rowText = rows[i].textContent;
     lines.push(rows[i].textContent);
    
   }
    //alert(lines);

    //console.log(lines);
    var input = lines;
	var data = {uMsg : lines};
	
	var request = new XMLHttpRequest();
	request.open("POST", "http://localhost/mysite/views/sendrow.php");
	request.setRequestHeader("Content-Type", "application/json");
	request.overrideMimeType("text/plain");
	request.onload = function()
	{
		        var data = request.responseText;
            //console.log(data[0]);
            // alert(data[0]);
	};
	request.send(JSON.stringify(data));
} 

document.addEventListener('DOMContentLoaded', function() {
	document.getElementById("submit4").addEventListener("click", postUser);
});





</script>


<style>
table, td {
    border: 1px solid black;
}
</style>

</body>

<?php 
include "footer.php";
?>
</html>