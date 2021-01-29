<!DOCTYPE html>
<html lang="en">
<?php


        if(isset($_POST['text_box'])) { 
        $a = $_POST['text_box'];
        $myFile = "../users/mydata.txt";
        $fh = fopen($myFile, 'w') or die("can't open file");
        fwrite($fh, $a);
        fclose($fh);
    }
    
    
$command = "python ../python/grammar.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 usleep(100000);
}
pclose($pid);

$command = "python ../python/entity_attribute.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 usleep(100000);
}
pclose($pid);



$command = "python ../python/entity_attr_to_xml.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
echo fread($pid, 256);
flush();
ob_flush();
usleep(100000);
}
pclose($pid);


$myFile = "../users/entity1.txt";
$fh = fopen($myFile, 'w') or die("can't open file");
$myFile = "../users/entity2.txt";
$fh2 = fopen($myFile, 'w') or die("can't open file");

$xml = simplexml_load_file("../users/cell.xml");
$entity_c = count($xml->celldata->entity);
$entity_t=array($entity_c);

for($x=0; $x<$entity_c; $x++)
	{
	  $entity_t[$x]=$xml->celldata->entity[$x];
		#  echo $entity_t[$x]."<br>";
	}

for($z=0; $z<$entity_c; $z++)
{
	$entity[$z+1] = array();
	
	$entity[$z+1][0] = $entity_t[$z];
	//echo "".$entity[$z+1][0].",";
	$a = "".$entity[$z+1][0].",";
	fwrite($fh, $a);
	$attri_c = count($xml->celldata->Entity[$z]->Attributes);
		
		for($i=1; $i<=$attri_c; $i++)
		{
			$entity[$z+1][$i] =$xml->celldata->Entity[$z]->Attributes[$i-1];
			//echo $entity[$z+1][$i].",";
			$b = $entity[$z+1][$i].",";
            fwrite($fh, $b);
		}
	//echo "<br>";

	

	if($z != $entity_c-1){
	$c = "\r\n";
	fwrite($fh, $c);
	}
	 
}


$entity_relation_c = count($xml->celldata->entity_relation);
#echo $entity_relation_c;

$entity_relation=array($entity_relation_c);

for($x=0; $x<$entity_relation_c; $x++)
	{
	  $entity_relation[$x]=$xml->celldata->entity_relation[$x];
		# echo $entity_relation[$x]."<br>";
	}


for($i=0;$i<$entity_relation_c;)
{
	$y = $i/2;
	$entity_relationship[$y] = array(3);

	$entity_relationship[$y][0] = $entity_relation[$i];
	$entity_relationship[$y][1] = $entity_relation[$i+1];
	$entity_relationship[$y][2] = $xml->celldata->relationship[$y];



	//echo "entity name = ".$entity_relationship[$y][0]." entity name = ".$entity_relationship[$y][1]." relationship = ".$entity_relationship[$y][2];
	$e= "".$entity_relationship[$y][0].",".$entity_relationship[$y][2].",".$entity_relationship[$y][1];
	fwrite($fh2, $e);
	if($i !=  $entity_relation_c ){
	$h = "\r\n";
	 fwrite($fh2, $h);
	}
	//echo"<br>";
	

$i = $i+2;
} 

fclose($fh);
fclose($fh2);


?>

<head>
<link rel="stylesheet" type="text/css" href="css/sidebar-left.css">

</head>

<body>
<br><br>

	<aside class="sidebar-left">


        <div class="sidebar-links" style="padding-top: 10%;">
            <a class="link-yellow " name="2nf" href="RDBMS.php"><div align="center">RDBMS</div></a>
            <a class="link-green" href="ORDBMS.php"><div align="center">ORDBMS</div></a>
            <a class="link-pink" href="NOSQL.php"><div align="center">NOSQL</div></a>
        </div>
    
     
    </aside>

</body>

</html>