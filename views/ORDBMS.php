<?php 

		$command = "python ../python/schema.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);

		$command = "python ../python/new.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);
		
		$command = "python ../python/new1.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);
		
		$command = "python ../python/output1.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);
		
		$command = "python ../python/nor.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);

		$command = "python ../python/sql.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);

        $command = "python ../python/norma.py 2>&1";
        $pid = popen( $command,"r");
        while( !feof( $pid ) )
        {
        echo fread($pid, 256);
        flush();
        ob_flush();
        usleep(100000);
        }
        pclose($pid);
		
		$command = "python ../python/3nf.py 2>&1";
		$pid = popen( $command,"r");
		while( !feof( $pid ) )
		{
		echo fread($pid, 256);
		flush();
		ob_flush();
		usleep(100000);
		}
		pclose($pid);

        $command = "python ../python/ordbms.py 2>&1";
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

<div class="row">
<div class="col-sm-2"></div>
  <div class="col-sm-6">
	  
    
      <h3>ORDBMS Script</h3>
      <textarea rows="20" cols="77" spellcheck="true" name="text_box" id="text_box"> <?php $file = new SPLFileObject("../users/ORDBMS.txt");
foreach($file as $line) {
    echo $line;  }?> </textarea>

  </div>
<div class="col-sm-2"></div>


</br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br>
