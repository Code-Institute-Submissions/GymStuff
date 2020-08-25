{"filter":false,"title":"tests.py","tooltip":"/products/tests.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":152,"column":56},"end":{"row":152,"column":69},"action":"remove","lines":["shdescription"],"id":503},{"start":{"row":152,"column":56},"end":{"row":152,"column":73},"action":"insert","lines":["short_description"]}],[{"start":{"row":153,"column":56},"end":{"row":153,"column":57},"action":"insert","lines":["s"],"id":504},{"start":{"row":153,"column":57},"end":{"row":153,"column":58},"action":"insert","lines":["h"]}],[{"start":{"row":153,"column":56},"end":{"row":153,"column":69},"action":"remove","lines":["shdescription"],"id":505},{"start":{"row":153,"column":56},"end":{"row":153,"column":73},"action":"insert","lines":["short_description"]}],[{"start":{"row":153,"column":77},"end":{"row":153,"column":90},"action":"remove","lines":["door mounted "],"id":506}],[{"start":{"row":152,"column":77},"end":{"row":152,"column":83},"action":"remove","lines":["light "],"id":507}],[{"start":{"row":154,"column":34},"end":{"row":154,"column":40},"action":"remove","lines":["short_"],"id":508}],[{"start":{"row":155,"column":34},"end":{"row":155,"column":40},"action":"remove","lines":["short_"],"id":509}],[{"start":{"row":154,"column":55},"end":{"row":154,"column":61},"action":"remove","lines":["short_"],"id":510}],[{"start":{"row":155,"column":55},"end":{"row":155,"column":61},"action":"remove","lines":["short_"],"id":511}],[{"start":{"row":158,"column":10},"end":{"row":158,"column":17},"action":"remove","lines":[" short "],"id":512}],[{"start":{"row":158,"column":10},"end":{"row":158,"column":11},"action":"insert","lines":[" "],"id":513}],[{"start":{"row":159,"column":12},"end":{"row":159,"column":18},"action":"remove","lines":["_short"],"id":514}],[{"start":{"row":124,"column":11},"end":{"row":124,"column":15},"action":"remove","lines":["Name"],"id":515},{"start":{"row":124,"column":11},"end":{"row":124,"column":12},"action":"insert","lines":["S"]},{"start":{"row":124,"column":12},"end":{"row":124,"column":13},"action":"insert","lines":["h"]},{"start":{"row":124,"column":13},"end":{"row":124,"column":14},"action":"insert","lines":["p"]}],[{"start":{"row":124,"column":13},"end":{"row":124,"column":14},"action":"remove","lines":["p"],"id":516}],[{"start":{"row":124,"column":13},"end":{"row":124,"column":14},"action":"insert","lines":["o"],"id":517},{"start":{"row":124,"column":14},"end":{"row":124,"column":15},"action":"insert","lines":["r"]},{"start":{"row":124,"column":15},"end":{"row":124,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":124,"column":11},"end":{"row":124,"column":16},"action":"remove","lines":["Short"],"id":518},{"start":{"row":124,"column":11},"end":{"row":124,"column":28},"action":"insert","lines":["Short_description"]}],[{"start":{"row":120,"column":4},"end":{"row":120,"column":8},"action":"remove","lines":["    "],"id":519},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"remove","lines":["    "]},{"start":{"row":119,"column":98},"end":{"row":120,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":159,"column":11},"end":{"row":159,"column":15},"action":"remove","lines":["Name"],"id":520},{"start":{"row":159,"column":11},"end":{"row":159,"column":12},"action":"insert","lines":["D"]},{"start":{"row":159,"column":12},"end":{"row":159,"column":13},"action":"insert","lines":["e"]},{"start":{"row":159,"column":13},"end":{"row":159,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":159,"column":11},"end":{"row":159,"column":14},"action":"remove","lines":["Des"],"id":521},{"start":{"row":159,"column":11},"end":{"row":159,"column":22},"action":"insert","lines":["Description"]}],[{"start":{"row":166,"column":4},"end":{"row":199,"column":110},"action":"insert","lines":["###### DESCRIPTION TESTING ######","        ","    # Test description field of product model from name","    def test_description_from_name(self):","        \"\"\"Description correctly identified from name\"\"\"","        test_description_object_1 = Product.objects.get(name=\"10kg weight\")","        test_description_object_2 = Product.objects.get(name=\"pull up bar\")","        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')","        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar')","","    # Test description field of product model from category","    def test_description_from_category(self):","        \"\"\"Description correctly identified from category\"\"\"","        test_description_object_1 = Product.objects.get(category=\"Weights\")","        test_description_object_2 = Product.objects.get(category=\"Accessories\")","        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')","        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar')        ","        ","    # Test description field of product model from short description","    def test_description_from_short_description(self):","        \"\"\"Description correctly identified from short description\"\"\"","        test_description_object_1 = Product.objects.get(short_description=\"A weight plate\")","        test_description_object_2 = Product.objects.get(short_description=\"A pull up bar\")","        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')","        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar') ","        ","        ","    # Test description field of product model from price","    def test_description_from_price(self):","        \"\"\"Description correctly identified from price\"\"\"","        test_short_description_object_1 = Product.objects.get(price=\"50\")","        test_short_description_object_2 = Product.objects.get(price=\"30\")","        self.assertEqual(str(test_short_description_object_1.short_description), 'A light weight plate')","        self.assertEqual(str(test_short_description_object_2.short_description), 'A door mounted pull up bar')"],"id":522}],[{"start":{"row":166,"column":11},"end":{"row":166,"column":22},"action":"remove","lines":["DESCRIPTION"],"id":523},{"start":{"row":166,"column":11},"end":{"row":166,"column":12},"action":"insert","lines":["P"]},{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"insert","lines":["r"]},{"start":{"row":166,"column":13},"end":{"row":166,"column":14},"action":"insert","lines":["i"]},{"start":{"row":166,"column":14},"end":{"row":166,"column":15},"action":"insert","lines":["c"]},{"start":{"row":166,"column":15},"end":{"row":166,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":166,"column":15},"end":{"row":166,"column":16},"action":"remove","lines":["e"],"id":524},{"start":{"row":166,"column":14},"end":{"row":166,"column":15},"action":"remove","lines":["c"]},{"start":{"row":166,"column":13},"end":{"row":166,"column":14},"action":"remove","lines":["i"]},{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"remove","lines":["r"]}],[{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"insert","lines":["R"],"id":525},{"start":{"row":166,"column":13},"end":{"row":166,"column":14},"action":"insert","lines":["I"]},{"start":{"row":166,"column":14},"end":{"row":166,"column":15},"action":"insert","lines":["C"]},{"start":{"row":166,"column":15},"end":{"row":166,"column":16},"action":"insert","lines":["E"]}],[{"start":{"row":168,"column":11},"end":{"row":168,"column":22},"action":"remove","lines":["description"],"id":526},{"start":{"row":168,"column":11},"end":{"row":168,"column":12},"action":"insert","lines":["p"]},{"start":{"row":168,"column":12},"end":{"row":168,"column":13},"action":"insert","lines":["r"]},{"start":{"row":168,"column":13},"end":{"row":168,"column":14},"action":"insert","lines":["i"]},{"start":{"row":168,"column":14},"end":{"row":168,"column":15},"action":"insert","lines":["c"]},{"start":{"row":168,"column":15},"end":{"row":168,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":169,"column":13},"end":{"row":169,"column":24},"action":"remove","lines":["description"],"id":527},{"start":{"row":169,"column":13},"end":{"row":169,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":176,"column":11},"end":{"row":176,"column":23},"action":"remove","lines":["description "],"id":528},{"start":{"row":176,"column":11},"end":{"row":176,"column":16},"action":"insert","lines":["price"]}],[{"start":{"row":176,"column":16},"end":{"row":176,"column":17},"action":"insert","lines":[" "],"id":529}],[{"start":{"row":170,"column":11},"end":{"row":170,"column":22},"action":"remove","lines":["Description"],"id":530},{"start":{"row":170,"column":11},"end":{"row":170,"column":12},"action":"insert","lines":["P"]},{"start":{"row":170,"column":12},"end":{"row":170,"column":13},"action":"insert","lines":["r"]},{"start":{"row":170,"column":13},"end":{"row":170,"column":14},"action":"insert","lines":["i"]},{"start":{"row":170,"column":14},"end":{"row":170,"column":15},"action":"insert","lines":["c"]}],[{"start":{"row":170,"column":15},"end":{"row":170,"column":16},"action":"insert","lines":["c"],"id":531},{"start":{"row":170,"column":16},"end":{"row":170,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":170,"column":16},"end":{"row":170,"column":17},"action":"remove","lines":["e"],"id":532},{"start":{"row":170,"column":15},"end":{"row":170,"column":16},"action":"remove","lines":["c"]}],[{"start":{"row":170,"column":15},"end":{"row":170,"column":16},"action":"insert","lines":["e"],"id":533}],[{"start":{"row":178,"column":11},"end":{"row":178,"column":22},"action":"remove","lines":["Description"],"id":534},{"start":{"row":178,"column":11},"end":{"row":178,"column":12},"action":"insert","lines":["P"]},{"start":{"row":178,"column":12},"end":{"row":178,"column":13},"action":"insert","lines":["r"]},{"start":{"row":178,"column":13},"end":{"row":178,"column":14},"action":"insert","lines":["i"]},{"start":{"row":178,"column":14},"end":{"row":178,"column":15},"action":"insert","lines":["c"]},{"start":{"row":178,"column":15},"end":{"row":178,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":186,"column":11},"end":{"row":186,"column":22},"action":"remove","lines":["Description"],"id":535},{"start":{"row":186,"column":11},"end":{"row":186,"column":12},"action":"insert","lines":["P"]},{"start":{"row":186,"column":12},"end":{"row":186,"column":13},"action":"insert","lines":["r"]},{"start":{"row":186,"column":13},"end":{"row":186,"column":14},"action":"insert","lines":["i"]},{"start":{"row":186,"column":14},"end":{"row":186,"column":15},"action":"insert","lines":["c"]},{"start":{"row":186,"column":15},"end":{"row":186,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":195,"column":11},"end":{"row":195,"column":22},"action":"remove","lines":["Description"],"id":536},{"start":{"row":195,"column":11},"end":{"row":195,"column":12},"action":"insert","lines":["P"]},{"start":{"row":195,"column":12},"end":{"row":195,"column":13},"action":"insert","lines":["r"]},{"start":{"row":195,"column":13},"end":{"row":195,"column":14},"action":"insert","lines":["i"]},{"start":{"row":195,"column":14},"end":{"row":195,"column":15},"action":"insert","lines":["c"]},{"start":{"row":195,"column":15},"end":{"row":195,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":195,"column":43},"end":{"row":195,"column":48},"action":"remove","lines":["price"],"id":537},{"start":{"row":195,"column":43},"end":{"row":195,"column":44},"action":"insert","lines":["s"]},{"start":{"row":195,"column":44},"end":{"row":195,"column":45},"action":"insert","lines":["h"]},{"start":{"row":195,"column":45},"end":{"row":195,"column":46},"action":"insert","lines":["o"]},{"start":{"row":195,"column":46},"end":{"row":195,"column":47},"action":"insert","lines":["r"]},{"start":{"row":195,"column":47},"end":{"row":195,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":195,"column":47},"end":{"row":195,"column":48},"action":"remove","lines":["t"],"id":538},{"start":{"row":195,"column":46},"end":{"row":195,"column":47},"action":"remove","lines":["r"]},{"start":{"row":195,"column":45},"end":{"row":195,"column":46},"action":"remove","lines":["o"]},{"start":{"row":195,"column":44},"end":{"row":195,"column":45},"action":"remove","lines":["h"]},{"start":{"row":195,"column":43},"end":{"row":195,"column":44},"action":"remove","lines":["s"]}],[{"start":{"row":195,"column":43},"end":{"row":195,"column":44},"action":"insert","lines":["d"],"id":539},{"start":{"row":195,"column":44},"end":{"row":195,"column":45},"action":"insert","lines":["e"]},{"start":{"row":195,"column":45},"end":{"row":195,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":195,"column":43},"end":{"row":195,"column":46},"action":"remove","lines":["des"],"id":540},{"start":{"row":195,"column":43},"end":{"row":195,"column":54},"action":"insert","lines":["description"]}],[{"start":{"row":177,"column":13},"end":{"row":177,"column":24},"action":"remove","lines":["description"],"id":541},{"start":{"row":177,"column":13},"end":{"row":177,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":185,"column":13},"end":{"row":185,"column":24},"action":"remove","lines":["description"],"id":542},{"start":{"row":185,"column":13},"end":{"row":185,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":184,"column":11},"end":{"row":184,"column":22},"action":"remove","lines":["description"],"id":543},{"start":{"row":184,"column":11},"end":{"row":184,"column":16},"action":"insert","lines":["price"]}],[{"start":{"row":193,"column":11},"end":{"row":193,"column":22},"action":"remove","lines":["description"],"id":544},{"start":{"row":193,"column":11},"end":{"row":193,"column":16},"action":"insert","lines":["price"]}],[{"start":{"row":193,"column":45},"end":{"row":193,"column":50},"action":"remove","lines":["price"],"id":545},{"start":{"row":193,"column":45},"end":{"row":193,"column":46},"action":"insert","lines":["d"]},{"start":{"row":193,"column":46},"end":{"row":193,"column":47},"action":"insert","lines":["e"]},{"start":{"row":193,"column":47},"end":{"row":193,"column":48},"action":"insert","lines":["s"]},{"start":{"row":193,"column":48},"end":{"row":193,"column":49},"action":"insert","lines":["c"]},{"start":{"row":193,"column":49},"end":{"row":193,"column":50},"action":"insert","lines":["r"]},{"start":{"row":193,"column":50},"end":{"row":193,"column":51},"action":"insert","lines":["i"]}],[{"start":{"row":193,"column":51},"end":{"row":193,"column":52},"action":"insert","lines":["p"],"id":546},{"start":{"row":193,"column":52},"end":{"row":193,"column":53},"action":"insert","lines":["t"]},{"start":{"row":193,"column":53},"end":{"row":193,"column":54},"action":"insert","lines":["i"]},{"start":{"row":193,"column":54},"end":{"row":193,"column":55},"action":"insert","lines":["o"]},{"start":{"row":193,"column":55},"end":{"row":193,"column":56},"action":"insert","lines":["n"]}],[{"start":{"row":194,"column":12},"end":{"row":194,"column":13},"action":"insert","lines":["_"],"id":547},{"start":{"row":194,"column":13},"end":{"row":194,"column":14},"action":"insert","lines":["r"]},{"start":{"row":194,"column":14},"end":{"row":194,"column":15},"action":"insert","lines":["p"]}],[{"start":{"row":194,"column":14},"end":{"row":194,"column":15},"action":"remove","lines":["p"],"id":548},{"start":{"row":194,"column":13},"end":{"row":194,"column":14},"action":"remove","lines":["r"]}],[{"start":{"row":194,"column":13},"end":{"row":194,"column":14},"action":"insert","lines":["p"],"id":549},{"start":{"row":194,"column":14},"end":{"row":194,"column":15},"action":"insert","lines":["r"]},{"start":{"row":194,"column":15},"end":{"row":194,"column":16},"action":"insert","lines":["i"]},{"start":{"row":194,"column":16},"end":{"row":194,"column":17},"action":"insert","lines":["c"]},{"start":{"row":194,"column":17},"end":{"row":194,"column":18},"action":"insert","lines":["e"]},{"start":{"row":194,"column":18},"end":{"row":194,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":194,"column":19},"end":{"row":194,"column":20},"action":"insert","lines":["f"],"id":550},{"start":{"row":194,"column":20},"end":{"row":194,"column":21},"action":"insert","lines":["r"]},{"start":{"row":194,"column":21},"end":{"row":194,"column":22},"action":"insert","lines":["o"]},{"start":{"row":194,"column":22},"end":{"row":194,"column":23},"action":"insert","lines":["m"]}],[{"start":{"row":194,"column":36},"end":{"row":194,"column":46},"action":"remove","lines":["from_price"],"id":551}],[{"start":{"row":160,"column":13},"end":{"row":160,"column":19},"action":"remove","lines":["short_"],"id":552}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":19},"action":"remove","lines":["short_"],"id":553}],[{"start":{"row":162,"column":34},"end":{"row":162,"column":40},"action":"remove","lines":["short_"],"id":554}],[{"start":{"row":163,"column":33},"end":{"row":163,"column":39},"action":"remove","lines":["_short"],"id":555}],[{"start":{"row":162,"column":55},"end":{"row":162,"column":61},"action":"remove","lines":["short_"],"id":556}],[{"start":{"row":163,"column":55},"end":{"row":163,"column":61},"action":"remove","lines":["short_"],"id":557}],[{"start":{"row":171,"column":13},"end":{"row":171,"column":24},"action":"remove","lines":["description"],"id":558},{"start":{"row":171,"column":13},"end":{"row":171,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":172,"column":13},"end":{"row":172,"column":24},"action":"remove","lines":["description"],"id":559},{"start":{"row":172,"column":13},"end":{"row":172,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":173,"column":34},"end":{"row":173,"column":46},"action":"remove","lines":["description_"],"id":560},{"start":{"row":173,"column":34},"end":{"row":173,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":173,"column":39},"end":{"row":173,"column":40},"action":"insert","lines":["_"],"id":561}],[{"start":{"row":173,"column":49},"end":{"row":173,"column":60},"action":"remove","lines":["description"],"id":562},{"start":{"row":173,"column":49},"end":{"row":173,"column":54},"action":"insert","lines":["price"]}],[{"start":{"row":174,"column":34},"end":{"row":174,"column":45},"action":"remove","lines":["description"],"id":563},{"start":{"row":174,"column":34},"end":{"row":174,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":174,"column":49},"end":{"row":174,"column":60},"action":"remove","lines":["description"],"id":564},{"start":{"row":174,"column":49},"end":{"row":174,"column":54},"action":"insert","lines":["price"]}],[{"start":{"row":173,"column":58},"end":{"row":173,"column":78},"action":"remove","lines":["A light weight plate"],"id":565},{"start":{"row":173,"column":58},"end":{"row":173,"column":59},"action":"insert","lines":["5"]},{"start":{"row":173,"column":59},"end":{"row":173,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":174,"column":58},"end":{"row":174,"column":84},"action":"remove","lines":["A door mounted pull up bar"],"id":566},{"start":{"row":174,"column":58},"end":{"row":174,"column":59},"action":"insert","lines":["3"]},{"start":{"row":174,"column":59},"end":{"row":174,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":179,"column":13},"end":{"row":179,"column":24},"action":"remove","lines":["description"],"id":567},{"start":{"row":179,"column":13},"end":{"row":179,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":180,"column":13},"end":{"row":180,"column":24},"action":"remove","lines":["description"],"id":568},{"start":{"row":180,"column":13},"end":{"row":180,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":181,"column":55},"end":{"row":181,"column":66},"action":"remove","lines":["description"],"id":569},{"start":{"row":181,"column":55},"end":{"row":181,"column":60},"action":"insert","lines":["price"]}],[{"start":{"row":182,"column":55},"end":{"row":182,"column":66},"action":"remove","lines":["description"],"id":570},{"start":{"row":182,"column":55},"end":{"row":182,"column":60},"action":"insert","lines":["price"]}],[{"start":{"row":181,"column":34},"end":{"row":181,"column":45},"action":"remove","lines":["description"],"id":571},{"start":{"row":181,"column":34},"end":{"row":181,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":182,"column":34},"end":{"row":182,"column":45},"action":"remove","lines":["description"],"id":572},{"start":{"row":182,"column":34},"end":{"row":182,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":181,"column":58},"end":{"row":181,"column":78},"action":"remove","lines":["A light weight plate"],"id":573},{"start":{"row":181,"column":58},"end":{"row":181,"column":59},"action":"insert","lines":["5"]},{"start":{"row":181,"column":59},"end":{"row":181,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":182,"column":58},"end":{"row":182,"column":84},"action":"remove","lines":["A door mounted pull up bar"],"id":574},{"start":{"row":182,"column":58},"end":{"row":182,"column":59},"action":"insert","lines":["3"]},{"start":{"row":182,"column":59},"end":{"row":182,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":187,"column":13},"end":{"row":187,"column":24},"action":"remove","lines":["description"],"id":575},{"start":{"row":187,"column":13},"end":{"row":187,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":188,"column":13},"end":{"row":188,"column":24},"action":"remove","lines":["description"],"id":576},{"start":{"row":188,"column":13},"end":{"row":188,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":189,"column":34},"end":{"row":189,"column":45},"action":"remove","lines":["description"],"id":577},{"start":{"row":189,"column":34},"end":{"row":189,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":190,"column":34},"end":{"row":190,"column":45},"action":"remove","lines":["description"],"id":578},{"start":{"row":190,"column":34},"end":{"row":190,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":189,"column":49},"end":{"row":189,"column":60},"action":"remove","lines":["description"],"id":579},{"start":{"row":189,"column":49},"end":{"row":189,"column":54},"action":"insert","lines":["price"]}],[{"start":{"row":190,"column":49},"end":{"row":190,"column":60},"action":"remove","lines":["description"],"id":580},{"start":{"row":190,"column":49},"end":{"row":190,"column":54},"action":"insert","lines":["price"]}],[{"start":{"row":189,"column":58},"end":{"row":189,"column":78},"action":"remove","lines":["A light weight plate"],"id":581},{"start":{"row":189,"column":58},"end":{"row":189,"column":59},"action":"insert","lines":["5"]},{"start":{"row":189,"column":59},"end":{"row":189,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":190,"column":58},"end":{"row":190,"column":84},"action":"remove","lines":["A door mounted pull up bar"],"id":582},{"start":{"row":190,"column":58},"end":{"row":190,"column":59},"action":"insert","lines":["3"]},{"start":{"row":190,"column":59},"end":{"row":190,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":196,"column":62},"end":{"row":196,"column":67},"action":"remove","lines":["price"],"id":583},{"start":{"row":196,"column":62},"end":{"row":196,"column":63},"action":"insert","lines":["d"]},{"start":{"row":196,"column":63},"end":{"row":196,"column":64},"action":"insert","lines":["e"]},{"start":{"row":196,"column":64},"end":{"row":196,"column":65},"action":"insert","lines":["s"]}],[{"start":{"row":196,"column":62},"end":{"row":196,"column":65},"action":"remove","lines":["des"],"id":584},{"start":{"row":196,"column":62},"end":{"row":196,"column":73},"action":"insert","lines":["description"]}],[{"start":{"row":197,"column":62},"end":{"row":197,"column":67},"action":"remove","lines":["price"],"id":585},{"start":{"row":197,"column":62},"end":{"row":197,"column":63},"action":"insert","lines":["d"]},{"start":{"row":197,"column":63},"end":{"row":197,"column":64},"action":"insert","lines":["e"]},{"start":{"row":197,"column":64},"end":{"row":197,"column":65},"action":"insert","lines":["s"]}],[{"start":{"row":197,"column":62},"end":{"row":197,"column":65},"action":"remove","lines":["des"],"id":586},{"start":{"row":197,"column":62},"end":{"row":197,"column":73},"action":"insert","lines":["description"]}],[{"start":{"row":196,"column":74},"end":{"row":196,"column":78},"action":"remove","lines":["\"50\""],"id":587},{"start":{"row":196,"column":74},"end":{"row":196,"column":96},"action":"insert","lines":["'A light weight plate'"]}],[{"start":{"row":197,"column":74},"end":{"row":197,"column":78},"action":"remove","lines":["\"30\""],"id":588},{"start":{"row":197,"column":74},"end":{"row":197,"column":102},"action":"insert","lines":["'A door mounted pull up bar'"]}],[{"start":{"row":198,"column":82},"end":{"row":198,"column":102},"action":"remove","lines":["A light weight plate"],"id":589},{"start":{"row":198,"column":82},"end":{"row":198,"column":83},"action":"insert","lines":["5"]},{"start":{"row":198,"column":83},"end":{"row":198,"column":84},"action":"insert","lines":["0"]}],[{"start":{"row":199,"column":82},"end":{"row":199,"column":108},"action":"remove","lines":["A door mounted pull up bar"],"id":590},{"start":{"row":199,"column":82},"end":{"row":199,"column":83},"action":"insert","lines":["3"]},{"start":{"row":199,"column":83},"end":{"row":199,"column":84},"action":"insert","lines":["0"]}],[{"start":{"row":196,"column":13},"end":{"row":196,"column":30},"action":"remove","lines":["short_description"],"id":591},{"start":{"row":196,"column":13},"end":{"row":196,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":197,"column":13},"end":{"row":197,"column":30},"action":"remove","lines":["short_description"],"id":592},{"start":{"row":197,"column":13},"end":{"row":197,"column":18},"action":"insert","lines":["price"]}],[{"start":{"row":198,"column":34},"end":{"row":198,"column":51},"action":"remove","lines":["short_description"],"id":593},{"start":{"row":198,"column":34},"end":{"row":198,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":198,"column":49},"end":{"row":198,"column":66},"action":"remove","lines":["short_description"],"id":594},{"start":{"row":198,"column":49},"end":{"row":198,"column":54},"action":"insert","lines":["price"]}],[{"start":{"row":199,"column":61},"end":{"row":199,"column":78},"action":"remove","lines":["short_description"],"id":595},{"start":{"row":199,"column":61},"end":{"row":199,"column":66},"action":"insert","lines":["price"]}],[{"start":{"row":199,"column":34},"end":{"row":199,"column":51},"action":"remove","lines":["short_description"],"id":596},{"start":{"row":199,"column":34},"end":{"row":199,"column":39},"action":"insert","lines":["price"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":597},{"start":{"row":5,"column":4},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":197,"column":60},"end":{"row":197,"column":61},"action":"insert","lines":["."],"id":598},{"start":{"row":197,"column":61},"end":{"row":197,"column":62},"action":"insert","lines":["0"]},{"start":{"row":197,"column":62},"end":{"row":197,"column":63},"action":"insert","lines":["0"]}],[{"start":{"row":198,"column":60},"end":{"row":198,"column":61},"action":"insert","lines":["."],"id":599},{"start":{"row":198,"column":61},"end":{"row":198,"column":62},"action":"insert","lines":["0"]},{"start":{"row":198,"column":62},"end":{"row":198,"column":63},"action":"insert","lines":["0"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":22},"action":"remove","lines":["50"],"id":600},{"start":{"row":13,"column":20},"end":{"row":13,"column":25},"action":"insert","lines":["50.00"]},{"start":{"row":53,"column":56},"end":{"row":53,"column":58},"action":"remove","lines":["50"]},{"start":{"row":53,"column":56},"end":{"row":53,"column":61},"action":"insert","lines":["50.00"]},{"start":{"row":88,"column":60},"end":{"row":88,"column":62},"action":"remove","lines":["50"]},{"start":{"row":88,"column":60},"end":{"row":88,"column":65},"action":"insert","lines":["50.00"]},{"start":{"row":123,"column":69},"end":{"row":123,"column":71},"action":"remove","lines":["50"]},{"start":{"row":123,"column":69},"end":{"row":123,"column":74},"action":"insert","lines":["50.00"]},{"start":{"row":159,"column":63},"end":{"row":159,"column":65},"action":"remove","lines":["50"]},{"start":{"row":159,"column":63},"end":{"row":159,"column":68},"action":"insert","lines":["50.00"]},{"start":{"row":172,"column":58},"end":{"row":172,"column":60},"action":"remove","lines":["50"]},{"start":{"row":172,"column":58},"end":{"row":172,"column":63},"action":"insert","lines":["50.00"]},{"start":{"row":180,"column":58},"end":{"row":180,"column":60},"action":"remove","lines":["50"]},{"start":{"row":180,"column":58},"end":{"row":180,"column":63},"action":"insert","lines":["50.00"]},{"start":{"row":188,"column":58},"end":{"row":188,"column":60},"action":"remove","lines":["50"]},{"start":{"row":188,"column":58},"end":{"row":188,"column":63},"action":"insert","lines":["50.00"]},{"start":{"row":197,"column":58},"end":{"row":197,"column":60},"action":"remove","lines":["50"]},{"start":{"row":197,"column":58},"end":{"row":197,"column":63},"action":"insert","lines":["50.00"]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":22},"action":"remove","lines":["30"],"id":601},{"start":{"row":20,"column":20},"end":{"row":20,"column":25},"action":"insert","lines":["30.00"]},{"start":{"row":54,"column":56},"end":{"row":54,"column":58},"action":"remove","lines":["30"]},{"start":{"row":54,"column":56},"end":{"row":54,"column":61},"action":"insert","lines":["30.00"]},{"start":{"row":89,"column":60},"end":{"row":89,"column":62},"action":"remove","lines":["30"]},{"start":{"row":89,"column":60},"end":{"row":89,"column":65},"action":"insert","lines":["30.00"]},{"start":{"row":124,"column":69},"end":{"row":124,"column":71},"action":"remove","lines":["30"]},{"start":{"row":124,"column":69},"end":{"row":124,"column":74},"action":"insert","lines":["30.00"]},{"start":{"row":160,"column":63},"end":{"row":160,"column":65},"action":"remove","lines":["30"]},{"start":{"row":160,"column":63},"end":{"row":160,"column":68},"action":"insert","lines":["30.00"]},{"start":{"row":173,"column":58},"end":{"row":173,"column":60},"action":"remove","lines":["30"]},{"start":{"row":173,"column":58},"end":{"row":173,"column":63},"action":"insert","lines":["30.00"]},{"start":{"row":181,"column":58},"end":{"row":181,"column":60},"action":"remove","lines":["30"]},{"start":{"row":181,"column":58},"end":{"row":181,"column":63},"action":"insert","lines":["30.00"]},{"start":{"row":189,"column":58},"end":{"row":189,"column":60},"action":"remove","lines":["30"]},{"start":{"row":189,"column":58},"end":{"row":189,"column":63},"action":"insert","lines":["30.00"]},{"start":{"row":198,"column":58},"end":{"row":198,"column":60},"action":"remove","lines":["30"]},{"start":{"row":198,"column":58},"end":{"row":198,"column":63},"action":"insert","lines":["30.00"]}],[{"start":{"row":197,"column":63},"end":{"row":197,"column":66},"action":"remove","lines":[".00"],"id":602}],[{"start":{"row":198,"column":63},"end":{"row":198,"column":66},"action":"remove","lines":[".00"],"id":603}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":29},"end":{"row":4,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1597668342821,"hash":"b9421aad102a2dfa43e7380e58c01eadcc97c81a"}