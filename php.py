<?php

$str = "Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg
<= 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu
dojrulwkp";

$len = strlen($str);

$result = "";

echo $str;

echo "<br/><br/>";

for($i=0; $i<$len; $i++)
{
	$ascii = ord($str[$i]);
	if($ascii < 65 || $ascii > 122 || ($ascii > 90 && $ascii < 97))
	$result .= $str[$i];
	else
	{
		if($ascii == 65) $ascii = 88;
		else if($ascii == 66) $ascii = 89;
		else if($ascii == 67) $ascii = 90;
		else if($ascii == 97) $ascii = 120;
		else if($ascii == 98) $ascii = 121;
		else if($ascii == 99) $ascii = 122;
		else $ascii = $ascii - 3;
		$char = chr($ascii);
		$result .= $char;
	}
}

echo $result."<br/><br/>"; ?>
