var colours = {
    green: "#4D9078",
    blue: "#00A7E1",
    red: "#DB504A",
    gray: "#BBBBBB"
};

var strokes = {
    black: "#000000",
    dark: "#444444"
};

var attr_blue = { fill: colours.blue, stroke: strokes.dark };
var attr_red = { fill: colours.red, stroke: strokes.dark };
var attr_green = { fill: colours.green, stroke: strokes.dark };
var attr_gray = { fill: colours.gray, stroke: strokes.dark };
var attr_poly = { fill: 'none', stroke: strokes.dark };

// Model 0

var mod0 = SVG("mod0").size(600, 600);
var mod0_c1 = mod0.circle(20).attr(attr_gray).x(260).y(90);
var mod0_c2 = mod0.circle(20).attr(attr_gray).x(260).y(111);
var mod0_c3 = mod0.circle(20).attr(attr_gray).x(260).y(132);
var mod0_c4 = mod0.circle(20).attr(attr_gray).x(260).y(153);
var mod0_tAS = mod0.text("AS").x(285).y(155);
var mod0_c5 = mod0.circle(20).attr(attr_gray).x(260).y(174);
var mod0_c6 = mod0.circle(20).attr(attr_gray).x(260).y(195);
var mod0_c7 = mod0.circle(20).attr(attr_gray).x(260).y(216);
var mod0_c8 = mod0.circle(20).attr(attr_blue).x(250).y(235);
var mod0_t8 = mod0.text("8").x(256).y(237);
var mod0_p8_14 = mod0.polyline([250,245, 156,256]).attr(attr_poly);
var mod0_c9 = mod0.circle(20).attr(attr_red).x(235).y(250);
var mod0_t9 = mod0.text("9").x(241).y(252);
var mod0_p9_23 = mod0.polyline([245,270, 245,288, 184,288, 184,301]).attr(attr_poly);
var mod0_c10 = mod0.circle(20).attr(attr_red).x(216).y(260);
var mod0_t10 = mod0.text("10").x(218).y(262);
var mod0_p10_45 = mod0.polyline([226,280, 226,293, 326,293, 326,322]).attr(attr_poly);
var mod0_c11 = mod0.circle(20).attr(attr_gray).x(195).y(260);
var mod0_c12 = mod0.circle(20).attr(attr_gray).x(174).y(260);
var mod0_c13 = mod0.circle(20).attr(attr_gray).x(153).y(260);
var mod0_c14 = mod0.circle(20).attr(attr_blue).x(136).y(246);
var mod0_p14_21 = mod0.polyline([146,266, 146,325]).attr(attr_poly);
var mod0_t14 = mod0.text("14").x(138).y(248);
var mod0_c15 = mod0.circle(20).attr(attr_blue).x(116).y(240);
var mod0_t15 = mod0.text("15").x(118).y(242);
var mod0_p15_48 = mod0.polyline([126,260, 126,298, 337,298]).attr(attr_poly);
var mod0_c16 = mod0.circle(20).attr(attr_gray).x(99).y(252);
var mod0_tDL = mod0.text("DL").x(60).y(262);
var mod0_c17 = mod0.circle(20).attr(attr_gray).x(89).y(270);
var mod0_c18 = mod0.circle(20).attr(attr_blue).x(89).y(291);
var mod0_t18 = mod0.text("18").x(91).y(293);
var mod0_t18_55 = mod0.polyline([96,311, 96,352, 456,352, 456,307]).attr(attr_poly);
var mod0_c19 = mod0.circle(20).attr(attr_blue).x(99).y(309);
var mod0_t19 = mod0.text("19").x(101).y(311);
var mod0_p19_56 = mod0.polyline([109,329, 109,373, 470,373, 470,289]).attr(attr_poly);
var mod0_c20 = mod0.circle(20).attr(attr_green).x(116).y(321);
var mod0_t20 = mod0.text("20").x(118).y(323);
var mod0_c21 = mod0.circle(20).attr(attr_blue).x(136).y(315);
var mod0_t21 = mod0.text("21").x(138).y(317);
var mod0_c22 = mod0.circle(20).attr(attr_blue).x(153).y(301);
var mod0_t22 = mod0.text("22").x(155).y(303);
var mod0_p22_46 = mod0.polyline([163,321, 163,394, 347,394, 347,342]).attr(attr_poly);
var mod0_c23 = mod0.circle(20).attr(attr_blue).x(174).y(301);
var mod0_t23 = mod0.text("23").x(176).y(303);
var mod0_tDS = mod0.text("DS").x(185).y(324);
var mod0_c24 = mod0.circle(20).attr(attr_gray).x(195).y(301);
var mod0_c25 = mod0.circle(20).attr(attr_gray).x(216).y(301);
var mod0_c26 = mod0.circle(20).attr(attr_blue).x(234).y(312);
var mod0_t26 = mod0.text("26").x(236).y(314);
var mod0_p26_44 = mod0.polyline([254,322, 298,322]).attr(attr_poly);
var mod0_c27 = mod0.circle(20).attr(attr_green).x(244).y(331);
var mod0_t27 = mod0.text("27").x(246).y(333);
var mod0_c28 = mod0.circle(20).attr(attr_green).x(244).y(352);
var mod0_t28 = mod0.text("28").x(246).y(354);
var mod0_c29 = mod0.circle(20).attr(attr_gray).x(244).y(373);
var mod0_tCS = mod0.text("CS").x(267).y(377);
var mod0_c30 = mod0.circle(20).attr(attr_gray).x(244).y(394);
var mod0_c31 = mod0.circle(20).attr(attr_green).x(244).y(415);
var mod0_t31 = mod0.text("31").x(246).y(417);
var mod0_c32 = mod0.circle(20).attr(attr_gray).x(230).y(431);
var mod0_c33 = mod0.circle(20).attr(attr_gray).x(230).y(452);
var mod0_c34 = mod0.circle(20).attr(attr_green).x(246).y(466);
var mod0_t34 = mod0.text("34").x(248).y(468);
var mod0_c35 = mod0.circle(20).attr(attr_gray).x(266).y(474);
var mod0_c36 = mod0.circle(20).attr(attr_gray).x(286).y(466);
var mod0_tCL = mod0.text("CL").x(298).y(490);
var mod0_c37 = mod0.circle(20).attr(attr_green).x(302).y(452);
var mod0_t37 = mod0.text("37").x(304).y(454);
var mod0_c38 = mod0.circle(20).attr(attr_gray).x(302).y(431);
var mod0_c39 = mod0.circle(20).attr(attr_green).x(288).y(415);
var mod0_t39 = mod0.text("39").x(290).y(417);
var mod0_c40 = mod0.circle(20).attr(attr_green).x(288).y(394);
var mod0_t40 = mod0.text("40").x(290).y(396);
var mod0_c41 = mod0.circle(20).attr(attr_gray).x(288).y(373);
var mod0_c42 = mod0.circle(20).attr(attr_gray).x(288).y(352);
var mod0_c43 = mod0.circle(20).attr(attr_gray).x(288).y(331);
var mod0_c44 = mod0.circle(20).attr(attr_blue).x(298).y(312);
var mod0_t44 = mod0.text("44").x(300).y(314);
var mod0_c45 = mod0.circle(20).attr(attr_blue).x(316).y(322);
var mod0_t45 = mod0.text("45").x(318).y(324);
var mod0_c46 = mod0.circle(20).attr(attr_blue).x(337).y(322);
var mod0_t46 = mod0.text("46").x(339).y(324);
var mod0_tVL = mod0.text("VL").x(370).y(328);
var mod0_c47 = mod0.circle(20).attr(attr_gray).x(351).y(306);
var mod0_c48 = mod0.circle(20).attr(attr_red).x(337).y(290);
var mod0_t48 = mod0.text("48").x(339).y(292);
var mod0_c49 = mod0.circle(20).attr(attr_gray).x(327).y(271);
var mod0_c50 = mod0.circle(20).attr(attr_gray).x(348).y(271);
var mod0_c51 = mod0.circle(20).attr(attr_gray).x(369).y(271);
var mod0_tTS = mod0.text("TS").x(370).y(252);
var mod0_c52 = mod0.circle(20).attr(attr_gray).x(390).y(271);
var mod0_c53 = mod0.circle(20).attr(attr_gray).x(411).y(271);
var mod0_c54 = mod0.circle(20).attr(attr_red).x(425).y(287);
var mod0_t54 = mod0.text("54").x(427).y(289);
var mod0_p54_58 = mod0.polyline([435,287, 458,239]).attr(attr_poly);
var mod0_c55 = mod0.circle(20).attr(attr_red).x(446).y(287);
var mod0_t55 = mod0.text("55").x(448).y(289);
var mod0_c56 = mod0.circle(20).attr(attr_blue).x(458).y(269);
var mod0_t56 = mod0.text("56").x(460).y(271);
var mod0_c57 = mod0.circle(20).attr(attr_gray).x(466).y(249);
var mod0_c58 = mod0.circle(20).attr(attr_red).x(458).y(229);
var mod0_t58 = mod0.text("58").x(460).y(231);
var mod0_tTL = mod0.text("TL").x(482).y(218);
var mod0_c59 = mod0.circle(20).attr(attr_gray).x(446).y(211);
var mod0_c60 = mod0.circle(20).attr(attr_gray).x(425).y(211);
var mod0_c61 = mod0.circle(20).attr(attr_gray).x(411).y(227);
var mod0_c62 = mod0.circle(20).attr(attr_gray).x(390).y(227);
var mod0_c63 = mod0.circle(20).attr(attr_gray).x(369).y(227);
var mod0_c64 = mod0.circle(20).attr(attr_gray).x(348).y(227);
var mod0_c65 = mod0.circle(20).attr(attr_gray).x(327).y(227);
var mod0_c66 = mod0.circle(20).attr(attr_gray).x(309).y(216);
var mod0_c67 = mod0.circle(20).attr(attr_gray).x(309).y(195);
var mod0_c68 = mod0.circle(20).attr(attr_gray).x(309).y(174);
var mod0_c69 = mod0.circle(20).attr(attr_gray).x(309).y(153);
var mod0_c70 = mod0.circle(20).attr(attr_gray).x(309).y(132);
var mod0_c71 = mod0.circle(20).attr(attr_gray).x(309).y(111);
var mod0_c72 = mod0.circle(20).attr(attr_gray).x(309).y(90);
var mod0_c73 = mod0.circle(20).attr(attr_gray).x(309).y(69);
var mod0_cC1 = mod0.circle(20).attr(attr_gray).x(309).y(48);
var mod0_tC1 = mod0.text("C").x(314).y(50);
var mod0_cC2 = mod0.circle(20).attr(attr_gray).x(309).y(27);
var mod0_tC2 = mod0.text("C").x(314).y(29);
var mod0_cA = mod0.circle(20).attr(attr_gray).x(309).y(6);
var mod0_tA = mod0.text("A").x(314).y(8);

// Model 1

var mod1 = SVG("mod1").size(600, 600);
var mod1_c1 = mod1.circle(20).attr(attr_gray).x(260).y(90);
var mod1_c2 = mod1.circle(20).attr(attr_gray).x(260).y(111);
var mod1_c3 = mod1.circle(20).attr(attr_gray).x(260).y(132);
var mod1_c4 = mod1.circle(20).attr(attr_gray).x(260).y(153);
var mod1_tAS = mod1.text("AS").x(288).y(155);
var mod1_c5 = mod1.circle(20).attr(attr_gray).x(260).y(174);
var mod1_c6 = mod1.circle(20).attr(attr_gray).x(260).y(195);
var mod1_c7 = mod1.circle(20).attr(attr_gray).x(260).y(216);
var mod1_c9 = mod1.circle(20).attr(attr_blue).x(250).y(235);
var mod1_t9 = mod1.text("9").x(256).y(237);
var mod1_p9_23 = mod1.polyline([260,255, 260,280, 203,280, 203,310]).attr(attr_poly);
var mod1_c10 = mod1.circle(20).attr(attr_blue).x(235).y(250);
var mod1_t10 = mod1.text("10").x(237).y(252);
var mod1_p10_45 = mod1.polyline([255,262, 315,262, 340,318]).attr(attr_poly);
var mod1_c11 = mod1.circle(20).attr(attr_gray).x(214).y(250);
var mod1_c12 = mod1.circle(20).attr(attr_gray).x(193).y(250);
var mod1_c13 = mod1.circle(20).attr(attr_gray).x(172).y(250);
var mod1_c14 = mod1.circle(20).attr(attr_gray).x(153).y(240);
var mod1_c15 = mod1.circle(20).attr(attr_blue).x(135).y(252);
var mod1_t15 = mod1.text("15").x(137).y(254);
var mod1_p15_59 = mod1.polyline([145,252, 145,195, 459,195, 459,216]).attr(attr_poly);
var mod1_tDL = mod1.text("DL").x(105).y(250);
var mod1_c18 = mod1.circle(20).attr(attr_blue).x(123).y(270);
var mod1_t18 = mod1.text("18").x(125).y(272);
var mod1_t18_55 = mod1.polyline([131,290, 131,366, 459,366, 459,312]).attr(attr_poly);
var mod1_c19 = mod1.circle(20).attr(attr_blue).x(135).y(288);
var mod1_t19 = mod1.text("19").x(137).y(290);
var mod1_p19_56 = mod1.polyline([145,308, 145,387, 473,387, 473,294]).attr(attr_poly);
var mod1_c20 = mod1.circle(20).attr(attr_gray).x(153).y(300);
var mod1_c21 = mod1.circle(20).attr(attr_gray).x(172).y(290);
var mod1_c23 = mod1.circle(20).attr(attr_blue).x(193).y(290);
var mod1_t23 = mod1.text("23").x(195).y(292);
var mod1_tDS = mod1.text("DS").x(204).y(316);
var mod1_c24 = mod1.circle(20).attr(attr_gray).x(214).y(290);
var mod1_c25 = mod1.circle(20).attr(attr_gray).x(235).y(290);
var mod1_c26 = mod1.circle(20).attr(attr_blue).x(250).y(305);
var mod1_t26 = mod1.text("26").x(252).y(307);
var mod1_p26_44 = mod1.polyline([270,315, 314,315]).attr(attr_poly);
var mod1_c27a = mod1.circle(20).attr(attr_blue).x(260).y(324);
var mod1_t27a = mod1.text("27a").x(258).y(326);
var mod1_p27_43 = mod1.polyline([280,334, 304,334]).attr(attr_poly);
var mod1_c27b = mod1.circle(20).attr(attr_gray).x(260).y(345);
var mod1_c28 = mod1.circle(20).attr(attr_green).x(260).y(366);
var mod1_t28 = mod1.text("28").x(262).y(368);
var mod1_c29 = mod1.circle(20).attr(attr_green).x(260).y(387);
var mod1_t29 = mod1.text("29").x(262).y(389);
var mod1_tCS = mod1.text("CS").x(282).y(395);
var mod1_c30 = mod1.circle(20).attr(attr_gray).x(260).y(408);
var mod1_c31 = mod1.circle(20).attr(attr_gray).x(260).y(429);
var mod1_c32 = mod1.circle(20).attr(attr_green).x(246).y(445);
var mod1_t32 = mod1.text("32").x(248).y(447);
var mod1_c33 = mod1.circle(20).attr(attr_gray).x(246).y(466);
var mod1_c34 = mod1.circle(20).attr(attr_gray).x(262).y(480);
var mod1_c35 = mod1.circle(20).attr(attr_gray).x(282).y(488);
var mod1_c36 = mod1.circle(20).attr(attr_gray).x(302).y(480);
var mod1_tCL = mod1.text("CL").x(316).y(504);
var mod1_c37 = mod1.circle(20).attr(attr_green).x(318).y(466);
var mod1_t37 = mod1.text("37").x(320).y(468);
var mod1_c38 = mod1.circle(20).attr(attr_gray).x(318).y(445);
var mod1_c39 = mod1.circle(20).attr(attr_gray).x(304).y(429);
var mod1_c40 = mod1.circle(20).attr(attr_gray).x(304).y(408);
var mod1_c41 = mod1.circle(20).attr(attr_gray).x(304).y(387);
var mod1_c42 = mod1.circle(20).attr(attr_gray).x(304).y(366);
var mod1_c43 = mod1.circle(20).attr(attr_gray).x(304).y(345);
var mod1_c43a = mod1.circle(20).attr(attr_blue).x(304).y(324);
var mod1_t43a = mod1.text("43a").x(302).y(326);
var mod1_c44 = mod1.circle(20).attr(attr_blue).x(314).y(305);
var mod1_t44 = mod1.text("44").x(316).y(307);
var mod1_c45 = mod1.circle(20).attr(attr_blue).x(333).y(315);
var mod1_t45 = mod1.text("45").x(334).y(317);
var mod1_tVL = mod1.text("VL").x(362).y(317);
var mod1_c48 = mod1.circle(20).attr(attr_gray).x(340).y(295);
var mod1_c49 = mod1.circle(20).attr(attr_gray).x(330).y(276);
var mod1_c50 = mod1.circle(20).attr(attr_gray).x(351).y(276);
var mod1_c51 = mod1.circle(20).attr(attr_gray).x(372).y(276);
var mod1_tTS = mod1.text("TS").x(374).y(256);
var mod1_c52 = mod1.circle(20).attr(attr_gray).x(393).y(276);
var mod1_c53 = mod1.circle(20).attr(attr_gray).x(414).y(276);
var mod1_c54 = mod1.circle(20).attr(attr_blue).x(428).y(292);
var mod1_t54 = mod1.text("54").x(430).y(294);
var mod1_p54_58 = mod1.polyline([438,292, 461,244]).attr(attr_poly);
var mod1_c55 = mod1.circle(20).attr(attr_red).x(449).y(292);
var mod1_t55 = mod1.text("55").x(451).y(294);
var mod1_c56 = mod1.circle(20).attr(attr_blue).x(461).y(274);
var mod1_t56 = mod1.text("56").x(463).y(276);
var mod1_c57 = mod1.circle(20).attr(attr_gray).x(469).y(254);
var mod1_c58 = mod1.circle(20).attr(attr_red).x(461).y(234);
var mod1_t58 = mod1.text("58").x(463).y(236);
var mod1_tTL = mod1.text("TL").x(482).y(218);
var mod1_c59 = mod1.circle(20).attr(attr_blue).x(449).y(216);
var mod1_t59 = mod1.text("59").x(451).y(218);
var mod1_c60 = mod1.circle(20).attr(attr_gray).x(428).y(216);
var mod1_c61 = mod1.circle(20).attr(attr_gray).x(414).y(232);
var mod1_c62 = mod1.circle(20).attr(attr_gray).x(393).y(232);
var mod1_c63 = mod1.circle(20).attr(attr_gray).x(372).y(232);
var mod1_c64 = mod1.circle(20).attr(attr_gray).x(351).y(232);
var mod1_c65 = mod1.circle(20).attr(attr_gray).x(330).y(232);
var mod1_c66 = mod1.circle(20).attr(attr_gray).x(316).y(216);
var mod1_c67 = mod1.circle(20).attr(attr_gray).x(316).y(195);
var mod1_c68 = mod1.circle(20).attr(attr_gray).x(316).y(174);
var mod1_c69 = mod1.circle(20).attr(attr_gray).x(316).y(153);
var mod1_c70 = mod1.circle(20).attr(attr_gray).x(316).y(132);
var mod1_c71 = mod1.circle(20).attr(attr_gray).x(316).y(111);
var mod1_c72 = mod1.circle(20).attr(attr_gray).x(316).y(90);
var mod1_c73 = mod1.circle(20).attr(attr_gray).x(316).y(69);
var mod1_cC1 = mod1.circle(20).attr(attr_gray).x(316).y(48);
var mod1_tC1 = mod1.text("C").x(321).y(50);
var mod1_cC2 = mod1.circle(20).attr(attr_gray).x(316).y(27);
var mod1_tC2 = mod1.text("C").x(321).y(29);
var mod1_cA = mod1.circle(20).attr(attr_gray).x(316).y(6);
var mod1_tA = mod1.text("A").x(321).y(8);

// Model 2

var mod2 = SVG("mod2").size(600, 600);
var mod2_c1 = mod2.circle(20).attr(attr_gray).x(260).y(90);
var mod2_c2 = mod2.circle(20).attr(attr_gray).x(260).y(111);
var mod2_c3 = mod2.circle(20).attr(attr_gray).x(260).y(132);
var mod2_c4 = mod2.circle(20).attr(attr_gray).x(260).y(153);
var mod2_tAS = mod2.text("AS").x(285).y(155);
var mod2_c5 = mod2.circle(20).attr(attr_gray).x(260).y(174);
var mod2_c6 = mod2.circle(20).attr(attr_gray).x(260).y(195);
var mod2_c7 = mod2.circle(20).attr(attr_gray).x(260).y(216);
var mod2_c8 = mod2.circle(20).attr(attr_blue).x(250).y(235);
var mod2_t8 = mod2.text("8").x(256).y(237);
var mod2_p8_14 = mod2.polyline([250,245, 156,256]).attr(attr_poly);
var mod2_c9 = mod2.circle(20).attr(attr_red).x(235).y(250);
var mod2_t9 = mod2.text("9").x(241).y(252);
var mod2_p9_23 = mod2.polyline([245,270, 245,288, 184,288, 184,301]).attr(attr_poly);
var mod2_c10 = mod2.circle(20).attr(attr_red).x(216).y(260);
var mod2_t10 = mod2.text("10").x(218).y(262);
var mod2_p10_45 = mod2.polyline([226,280, 226,293, 326,293, 326,322]).attr(attr_poly);
var mod2_c11 = mod2.circle(20).attr(attr_gray).x(195).y(260);
var mod2_c12 = mod2.circle(20).attr(attr_gray).x(174).y(260);
var mod2_c13 = mod2.circle(20).attr(attr_gray).x(153).y(260);
var mod2_c14 = mod2.circle(20).attr(attr_blue).x(136).y(246);
var mod2_t14 = mod2.text("14").x(138).y(248);
var mod2_c15 = mod2.circle(20).attr(attr_blue).x(116).y(240);
var mod2_t15 = mod2.text("15").x(118).y(242);
var mod2_p15_48 = mod2.polyline([126,260, 126,298, 337,298]).attr(attr_poly);
var mod2_c16 = mod2.circle(20).attr(attr_gray).x(99).y(252);
var mod2_tDL = mod2.text("DL").x(60).y(262);
var mod2_c17 = mod2.circle(20).attr(attr_gray).x(89).y(270);
var mod2_c18 = mod2.circle(20).attr(attr_gray).x(89).y(291);
var mod2_c19 = mod2.circle(20).attr(attr_gray).x(99).y(309);
var mod2_c20 = mod2.circle(20).attr(attr_gray).x(116).y(321);
var mod2_c21 = mod2.circle(20).attr(attr_gray).x(136).y(315);
var mod2_c22 = mod2.circle(20).attr(attr_blue).x(153).y(301);
var mod2_t22 = mod2.text("22").x(155).y(303);
var mod2_p22_46 = mod2.polyline([163,321, 163,373, 347,373, 347,342]).attr(attr_poly);
var mod2_c23 = mod2.circle(20).attr(attr_blue).x(174).y(301);
var mod2_t23 = mod2.text("23").x(176).y(303);
var mod2_tDS = mod2.text("DS").x(185).y(324);
var mod2_c24 = mod2.circle(20).attr(attr_gray).x(195).y(301);
var mod2_c25 = mod2.circle(20).attr(attr_gray).x(216).y(301);
var mod2_c26 = mod2.circle(20).attr(attr_red).x(234).y(312);
var mod2_t26 = mod2.text("26").x(236).y(314);
var mod2_p26_44 = mod2.polyline([254,322, 298,322]).attr(attr_poly);
var mod2_c27 = mod2.circle(20).attr(attr_green).x(244).y(331);
var mod2_t27 = mod2.text("27").x(246).y(333);
var mod2_c28 = mod2.circle(20).attr(attr_green).x(244).y(352);
var mod2_t28 = mod2.text("28").x(246).y(354);
var mod2_c29 = mod2.circle(20).attr(attr_gray).x(244).y(373);
var mod2_tCS = mod2.text("CS").x(266).y(377);
var mod2_c30 = mod2.circle(20).attr(attr_gray).x(244).y(394);
var mod2_c31 = mod2.circle(20).attr(attr_gray).x(244).y(415);
var mod2_c32 = mod2.circle(20).attr(attr_green).x(230).y(431);
var mod2_t32 = mod2.text("32").x(232).y(433);
var mod2_c33 = mod2.circle(20).attr(attr_gray).x(230).y(452);
var mod2_c34 = mod2.circle(20).attr(attr_green).x(246).y(466);
var mod2_t34 = mod2.text("34").x(248).y(468);
var mod2_c35 = mod2.circle(20).attr(attr_gray).x(266).y(474);
var mod2_c36 = mod2.circle(20).attr(attr_gray).x(286).y(466);
var mod2_tCL = mod2.text("CL").x(298).y(490);
var mod2_c37 = mod2.circle(20).attr(attr_green).x(302).y(452);
var mod2_t37 = mod2.text("37").x(304).y(454);
var mod2_c38 = mod2.circle(20).attr(attr_green).x(302).y(431);
var mod2_t38 = mod2.text("38").x(304).y(433);
var mod2_c39 = mod2.circle(20).attr(attr_green).x(288).y(415);
var mod2_t39 = mod2.text("39").x(290).y(417);
var mod2_c40 = mod2.circle(20).attr(attr_green).x(288).y(394);
var mod2_t40 = mod2.text("40").x(290).y(396);
var mod2_c41 = mod2.circle(20).attr(attr_gray).x(288).y(373);
var mod2_c42 = mod2.circle(20).attr(attr_gray).x(288).y(352);
var mod2_c43 = mod2.circle(20).attr(attr_gray).x(288).y(331);
var mod2_c44 = mod2.circle(20).attr(attr_blue).x(298).y(312);
var mod2_t44 = mod2.text("44").x(300).y(314);
var mod2_c45 = mod2.circle(20).attr(attr_blue).x(316).y(322);
var mod2_t45 = mod2.text("45").x(318).y(324);
var mod2_c46 = mod2.circle(20).attr(attr_blue).x(337).y(322);
var mod2_t46 = mod2.text("46").x(339).y(324);
var mod2_tVL = mod2.text("VL").x(370).y(328);
var mod2_c47 = mod2.circle(20).attr(attr_gray).x(351).y(306);
var mod2_c48 = mod2.circle(20).attr(attr_blue).x(337).y(290);
var mod2_t48 = mod2.text("48").x(339).y(292);
var mod2_c49 = mod2.circle(20).attr(attr_green).x(327).y(271);
var mod2_t49 = mod2.text("49").x(329).y(273);
var mod2_c50 = mod2.circle(20).attr(attr_green).x(348).y(271);
var mod2_t50 = mod2.text("50").x(350).y(273);
var mod2_c51 = mod2.circle(20).attr(attr_gray).x(369).y(271);
var mod2_tTS = mod2.text("TS").x(372).y(252);
var mod2_c52 = mod2.circle(20).attr(attr_gray).x(390).y(271);
var mod2_c53 = mod2.circle(20).attr(attr_gray).x(411).y(271);
var mod2_c54 = mod2.circle(20).attr(attr_green).x(425).y(287);
var mod2_t54 = mod2.text("54").x(427).y(289);
var mod2_c55 = mod2.circle(20).attr(attr_green).x(446).y(287);
var mod2_t55 = mod2.text("55").x(448).y(289);
var mod2_c56 = mod2.circle(20).attr(attr_gray).x(458).y(269);
var mod2_c57 = mod2.circle(20).attr(attr_gray).x(466).y(249);
var mod2_c58 = mod2.circle(20).attr(attr_green).x(458).y(229);
var mod2_t58 = mod2.text("58").x(460).y(231);
var mod2_tTL = mod2.text("TL").x(482).y(218);
var mod2_c59 = mod2.circle(20).attr(attr_gray).x(446).y(211);
var mod2_c60 = mod2.circle(20).attr(attr_gray).x(425).y(211);
var mod2_c61 = mod2.circle(20).attr(attr_gray).x(411).y(227);
var mod2_c62 = mod2.circle(20).attr(attr_gray).x(390).y(227);
var mod2_c63 = mod2.circle(20).attr(attr_gray).x(369).y(227);
var mod2_c64 = mod2.circle(20).attr(attr_gray).x(348).y(227);
var mod2_c65 = mod2.circle(20).attr(attr_gray).x(327).y(227);
var mod2_c66 = mod2.circle(20).attr(attr_gray).x(309).y(216);
var mod2_c67 = mod2.circle(20).attr(attr_gray).x(309).y(195);
var mod2_c68 = mod2.circle(20).attr(attr_gray).x(309).y(174);
var mod2_c69 = mod2.circle(20).attr(attr_gray).x(309).y(153);
var mod2_c70 = mod2.circle(20).attr(attr_gray).x(309).y(132);
var mod2_c71 = mod2.circle(20).attr(attr_gray).x(309).y(111);
var mod2_c72 = mod2.circle(20).attr(attr_green).x(309).y(90);
var mod2_t72 = mod2.text("72").x(311).y(92);
var mod2_c73 = mod2.circle(20).attr(attr_gray).x(309).y(69);
var mod2_cC1 = mod2.circle(20).attr(attr_gray).x(309).y(48);
var mod2_tC1 = mod2.text("C").x(314).y(50);
var mod2_cC2 = mod2.circle(20).attr(attr_gray).x(309).y(27);
var mod2_tC2 = mod2.text("C").x(314).y(29);
var mod2_cA = mod2.circle(20).attr(attr_gray).x(309).y(6);
var mod2_tA = mod2.text("A").x(314).y(8);

// Model 3

var mod3 = SVG("mod3").size(600, 600);
var mod3_c1 = mod3.circle(20).attr(attr_gray).x(260).y(90);
var mod3_c2 = mod3.circle(20).attr(attr_gray).x(260).y(111);
var mod3_c3 = mod3.circle(20).attr(attr_gray).x(260).y(132);
var mod3_c4 = mod3.circle(20).attr(attr_gray).x(260).y(153);
var mod3_tAS = mod3.text("AS").x(288).y(155);
var mod3_c5 = mod3.circle(20).attr(attr_gray).x(260).y(174);
var mod3_c6 = mod3.circle(20).attr(attr_gray).x(260).y(195);
var mod3_c7 = mod3.circle(20).attr(attr_gray).x(260).y(216);
var mod3_c14 = mod3.circle(20).attr(attr_blue).x(250).y(235);
var mod3_t14 = mod3.text("14").x(252).y(237);
var mod3_p14_59 = mod3.polyline([270,247, 290,255, 440,255, 463,235]).attr(attr_poly);
var mod3_c15 = mod3.circle(20).attr(attr_blue).x(238).y(253);
var mod3_t15 = mod3.text("15").x(240).y(255);
var mod3_p15_59 = mod3.polyline([258,263, 446,263, 475,238]).attr(attr_poly);
var mod3_tDL = mod3.text("DL").x(202).y(265);
var mod3_c18 = mod3.circle(20).attr(attr_blue).x(230).y(273);
var mod3_t18 = mod3.text("18").x(232).y(275);
var mod3_p18_57 = mod3.polyline([250,283, 290,273, 484,273]).attr(attr_poly);
var mod3_c19 = mod3.circle(20).attr(attr_blue).x(230).y(294);
var mod3_t19 = mod3.text("19").x(232).y(296);
var mod3_p19_45 = mod3.polyline([250,304, 312,310]).attr(attr_poly);
var mod3_c27a = mod3.circle(20).attr(attr_blue).x(242).y(312);
var mod3_t27a = mod3.text("27a").x(240).y(314);
var mod3_p27_43 = mod3.polyline([262,322, 286,322]).attr(attr_poly);
var mod3_c27b = mod3.circle(20).attr(attr_gray).x(242).y(333);
var mod3_c28 = mod3.circle(20).attr(attr_gray).x(242).y(354);
var mod3_c29 = mod3.circle(20).attr(attr_gray).x(242).y(375);
var mod3_tCS = mod3.text("CS").x(264).y(384);
var mod3_c30 = mod3.circle(20).attr(attr_gray).x(242).y(396);
var mod3_c31 = mod3.circle(20).attr(attr_gray).x(242).y(417);
var mod3_c32 = mod3.circle(20).attr(attr_gray).x(228).y(433);
var mod3_c33 = mod3.circle(20).attr(attr_gray).x(228).y(454);
var mod3_c34 = mod3.circle(20).attr(attr_gray).x(244).y(468);
var mod3_c35 = mod3.circle(20).attr(attr_gray).x(264).y(476);
var mod3_c36 = mod3.circle(20).attr(attr_gray).x(284).y(468);
var mod3_tCL = mod3.text("CL").x(312).y(484);
var mod3_c37 = mod3.circle(20).attr(attr_green).x(300).y(454);
var mod3_t37 = mod3.text("37").x(302).y(456);
var mod3_c38 = mod3.circle(20).attr(attr_gray).x(300).y(433);
var mod3_c39 = mod3.circle(20).attr(attr_gray).x(286).y(417);
var mod3_c40 = mod3.circle(20).attr(attr_gray).x(286).y(396);
var mod3_c41 = mod3.circle(20).attr(attr_gray).x(286).y(375);
var mod3_c42 = mod3.circle(20).attr(attr_gray).x(286).y(354);
var mod3_c43 = mod3.circle(20).attr(attr_gray).x(286).y(333);
var mod3_c43a = mod3.circle(20).attr(attr_blue).x(286).y(312);
var mod3_t43a = mod3.text("43a").x(284).y(314);
var mod3_c45 = mod3.circle(20).attr(attr_blue).x(307).y(307);
var mod3_t45 = mod3.text("45").x(309).y(309);
var mod3_tVL = mod3.text("VL").x(352).y(335);
var mod3_c46 = mod3.circle(20).attr(attr_blue).x(327).y(315);
var mod3_t46 = mod3.text("46").x(329).y(317);
var mod3_p46_57 = mod3.polyline([347,325, 496,325, 496,285]).attr(attr_poly);
var mod3_c48 = mod3.circle(20).attr(attr_gray).x(338).y(296);
var mod3_c49 = mod3.circle(20).attr(attr_gray).x(330).y(276);
var mod3_c50 = mod3.circle(20).attr(attr_gray).x(351).y(276);
var mod3_c51 = mod3.circle(20).attr(attr_gray).x(372).y(276);
var mod3_c52 = mod3.circle(20).attr(attr_gray).x(393).y(276);
var mod3_c53 = mod3.circle(20).attr(attr_gray).x(414).y(276);
var mod3_c54 = mod3.circle(20).attr(attr_blue).x(432).y(288);
var mod3_t54 = mod3.text("54").x(434).y(290);
var mod3_p54_58 = mod3.polyline([448,290, 486,256]).attr(attr_poly);
var mod3_c55 = mod3.circle(20).attr(attr_gray).x(453).y(293);
var mod3_c56 = mod3.circle(20).attr(attr_gray).x(472).y(283);
var mod3_c57 = mod3.circle(20).attr(attr_blue).x(484).y(265);
var mod3_t57 = mod3.text("57").x(486).y(267);
var mod3_c58 = mod3.circle(20).attr(attr_red).x(484).y(243);
var mod3_t58 = mod3.text("58").x(486).y(245);
var mod3_tTL = mod3.text("TL").x(502).y(218);
var mod3_c59 = mod3.circle(20).attr(attr_blue).x(472).y(225);
var mod3_t59 = mod3.text("59").x(474).y(227);
var mod3_c59a = mod3.circle(20).attr(attr_blue).x(453).y(215);
var mod3_t59a = mod3.text("59a").x(451).y(217);
var mod3_c60 = mod3.circle(20).attr(attr_gray).x(432).y(220);
var mod3_c61 = mod3.circle(20).attr(attr_gray).x(414).y(232);
var mod3_tTS = mod3.text("TS").x(382).y(212);
var mod3_c62 = mod3.circle(20).attr(attr_gray).x(393).y(232);
var mod3_c63 = mod3.circle(20).attr(attr_gray).x(372).y(232);
var mod3_c64 = mod3.circle(20).attr(attr_gray).x(351).y(232);
var mod3_c65 = mod3.circle(20).attr(attr_gray).x(330).y(232);
var mod3_c66 = mod3.circle(20).attr(attr_gray).x(316).y(216);
var mod3_c67 = mod3.circle(20).attr(attr_gray).x(316).y(195);
var mod3_c68 = mod3.circle(20).attr(attr_gray).x(316).y(174);
var mod3_c69 = mod3.circle(20).attr(attr_gray).x(316).y(153);
var mod3_c70 = mod3.circle(20).attr(attr_gray).x(316).y(132);
var mod3_c71 = mod3.circle(20).attr(attr_gray).x(316).y(111);
var mod3_c72 = mod3.circle(20).attr(attr_gray).x(316).y(90);
var mod3_c73 = mod3.circle(20).attr(attr_gray).x(316).y(69);
var mod3_cC1 = mod3.circle(20).attr(attr_gray).x(316).y(48);
var mod3_tC1 = mod3.text("C").x(321).y(50);
var mod3_cC2 = mod3.circle(20).attr(attr_gray).x(316).y(27);
var mod3_tC2 = mod3.text("C").x(321).y(29);
var mod3_cA = mod3.circle(20).attr(attr_gray).x(316).y(6);
var mod3_tA = mod3.text("A").x(321).y(8);
