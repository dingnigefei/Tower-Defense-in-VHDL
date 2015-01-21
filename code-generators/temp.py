import re

s = ''' dests(0).pos.x <= tov(0, 10);
			dests(0).pos.y <= tov(180, 9);
			dests(0).dir <= RightDir;
			dests(1).pos.x <= tov(30, 10);
			dests(1).pos.y <= tov(180, 9);
			dests(1).dir <= UpDir;
			dests(2).pos.x <= tov(30, 10);
			dests(2).pos.y <= tov(90, 9);
			dests(2).dir <= RightDir;
			dests(3).pos.x <= tov(60, 10);
			dests(3).pos.y <= tov(90, 9);
			dests(3).dir <= UpDir;
			dests(4).pos.x <= tov(60, 10);
			dests(4).pos.y <= tov(60, 9);
			dests(4).dir <= RightDir;
			dests(5).pos.x <= tov(90, 10);
			dests(5).pos.y <= tov(60, 9);
			dests(5).dir <= UpDir;
			dests(6).pos.x <= tov(90, 10);
			dests(6).pos.y <= tov(30, 9);
			dests(6).dir <= RightDir;
			dests(9).pos.x <= tov(120, 10);
			dests(9).pos.y <= tov(30, 9);
			dests(9).dir <= UpDir;
			dests(10).pos.x <= tov(120, 10);
			dests(10).pos.y <= tov(0, 9);
			dests(10).dir <= RightDir;
			dests(17).pos.x <= tov(330, 10);
			dests(17).pos.y <= tov(0, 9);
			dests(17).dir <= DownDir;
			dests(18).pos.x <= tov(330, 10);
			dests(18).pos.y <= tov(30, 9);
			dests(18).dir <= RightDir;
			dests(19).pos.x <= tov(360, 10);
			dests(19).pos.y <= tov(30, 9);
			dests(19).dir <= DownDir;
			dests(20).pos.x <= tov(360, 10);
			dests(20).pos.y <= tov(60, 9);
			dests(20).dir <= RightDir;
			dests(21).pos.x <= tov(390, 10);
			dests(21).pos.y <= tov(60, 9);
			dests(21).dir <= DownDir;
			dests(22).pos.x <= tov(390, 10);
			dests(22).pos.y <= tov(90, 9);
			dests(22).dir <= RightDir;
			dests(23).pos.x <= tov(420, 10);
			dests(23).pos.y <= tov(90, 9);
			dests(23).dir <= DownDir;
			dests(25).pos.x <= tov(420, 10);
			dests(25).pos.y <= tov(150, 9);
			dests(25).dir <= RightDir;
			dests(26).pos.x <= tov(450, 10);
			dests(26).pos.y <= tov(150, 9);
			dests(26).dir <= DownDir;
			dests(30).pos.x <= tov(450, 10);
			dests(30).pos.y <= tov(270, 9);
			dests(30).dir <= LeftDir;
			dests(36).pos.x <= tov(270, 10);
			dests(36).pos.y <= tov(270, 9);
			dests(36).dir <= UpDir;
			dests(38).pos.x <= tov(270, 10);
			dests(38).pos.y <= tov(210, 9);
			dests(38).dir <= LeftDir;
			dests(41).pos.x <= tov(180, 10);
			dests(41).pos.y <= tov(210, 9);
			dests(41).dir <= DownDir;
			dests(43).pos.x <= tov(180, 10);
			dests(43).pos.y <= tov(270, 9);
			dests(43).dir <= LeftDir;
			dests(49).pos.x <= tov(0, 10);
			dests(49).pos.y <= tov(270, 9);
			dests(49).dir <= DownDir;
			dests(51).pos.x <= tov(0, 10);
			dests(51).pos.y <= tov(330, 9);
			dests(51).dir <= RightDir;
			dests(52).pos.x <= tov(30, 10);
			dests(52).pos.y <= tov(330, 9);
			dests(52).dir <= DownDir;
			dests(53).pos.x <= tov(30, 10);
			dests(53).pos.y <= tov(360, 9);
			dests(53).dir <= RightDir;
			dests(54).pos.x <= tov(60, 10);
			dests(54).pos.y <= tov(360, 9);
			dests(54).dir <= DownDir;
			dests(55).pos.x <= tov(60, 10);
			dests(55).pos.y <= tov(390, 9);
			dests(55).dir <= RightDir;
			dests(56).pos.x <= tov(90, 10);
			dests(56).pos.y <= tov(390, 9);
			dests(56).dir <= DownDir;
			dests(57).pos.x <= tov(90, 10);
			dests(57).pos.y <= tov(420, 9);
			dests(57).dir <= RightDir;
			dests(58).pos.x <= tov(120, 10);
			dests(58).pos.y <= tov(420, 9);
			dests(58).dir <= DownDir;
			dests(59).pos.x <= tov(120, 10);
			dests(59).pos.y <= tov(450, 9);
			dests(59).dir <= RightDir;
			dests(66).pos.x <= tov(330, 10);
			dests(66).pos.y <= tov(450, 9);
			dests(66).dir <= UpDir;
			dests(67).pos.x <= tov(330, 10);
			dests(67).pos.y <= tov(420, 9);
			dests(67).dir <= RightDir;
			dests(68).pos.x <= tov(360, 10);
			dests(68).pos.y <= tov(420, 9);
			dests(68).dir <= UpDir;
			dests(69).pos.x <= tov(360, 10);
			dests(69).pos.y <= tov(390, 9);
			dests(69).dir <= RightDir;
			dests(70).pos.x <= tov(390, 10);
			dests(70).pos.y <= tov(390, 9);
			dests(70).dir <= UpDir;
			dests(71).pos.x <= tov(390, 10);
			dests(71).pos.y <= tov(360, 9);
			dests(71).dir <= RightDir;
			dests(72).pos.x <= tov(420, 10);
			dests(72).pos.y <= tov(360, 9);
			dests(72).dir <= UpDir;
			dests(73).pos.x <= tov(420, 10);
			dests(73).pos.y <= tov(330, 9);
			dests(73).dir <= RightDir;'''

l = s.splitlines()
for i in xrange(0, len(l), 3):
	outI = i / 3
	for j in xrange(3):
		print re.sub(r'\(\d+\)', '(%d)' % outI, l[i + j])
