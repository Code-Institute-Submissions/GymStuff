{"filter":false,"title":"tests.py","tooltip":"/physical/tests.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"remove","lines":["t"],"id":640}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["T"],"id":641}],[{"start":{"row":12,"column":33},"end":{"row":12,"column":36},"action":"remove","lines":["bmi"],"id":642},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"insert","lines":["B"]},{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"insert","lines":["M"]},{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":["I"]}],[{"start":{"row":10,"column":25},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":643},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":18,"column":47},"action":"insert","lines":["    # Get height from user id","    def test_get_height_from_user(self):","        \"\"\"Height correctly retrieved by user\"\"\"","        height1 = Physical.objects.get(user=1)","        height2 = Physical.objects.get(user=2)","        self.assertEqual(height1.height, 160.00)","        self.assertEqual(height2.height, 80.00)"],"id":644}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "],"id":645}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["t"],"id":646},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["h"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["g"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["i"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"remove","lines":["h"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["b"],"id":647},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["m"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["i"]}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":26},"action":"remove","lines":["from user id"],"id":648},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["r"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["e"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["s"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["u"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["l"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":[" "],"id":649},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["v"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["i"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["e"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["w"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":33},"action":"remove","lines":["get_height_from_user"],"id":650},{"start":{"row":13,"column":13},"end":{"row":13,"column":28},"action":"insert","lines":["bmi result view"]}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":[" "],"id":651}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["_"],"id":652}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":[" "],"id":653}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["_"],"id":654}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":46},"action":"remove","lines":["        height1 = Physical.objects.get(user=1)","        height2 = Physical.objects.get(user=2)"],"id":655},{"start":{"row":15,"column":0},"end":{"row":16,"column":24},"action":"insert","lines":["response = c.post('/login/', {'username': 'john', 'password': 'smith'})",">>> response.status_code"]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "],"id":656}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"insert","lines":["    "],"id":657}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":658}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":659}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":12},"action":"remove","lines":[">>> "],"id":660}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":79},"action":"remove","lines":["c.post('/login/', {'username': 'john', 'password': 'smith'})"],"id":661},{"start":{"row":15,"column":19},"end":{"row":15,"column":35},"action":"insert","lines":["c.get('/login/')"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":32},"action":"remove","lines":["login"],"id":662},{"start":{"row":15,"column":27},"end":{"row":15,"column":37},"action":"insert","lines":["bmi_result"]}],[{"start":{"row":17,"column":25},"end":{"row":17,"column":39},"action":"remove","lines":["height1.height"],"id":663},{"start":{"row":17,"column":25},"end":{"row":17,"column":45},"action":"insert","lines":["response.status_code"]}],[{"start":{"row":17,"column":47},"end":{"row":17,"column":53},"action":"remove","lines":["160.00"],"id":664},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"insert","lines":["2"]},{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"insert","lines":["0"]},{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["0"]}],[{"start":{"row":17,"column":51},"end":{"row":18,"column":47},"action":"remove","lines":["","        self.assertEqual(height2.height, 80.00)"],"id":665}],[{"start":{"row":15,"column":40},"end":{"row":16,"column":28},"action":"remove","lines":["","        response.status_code"],"id":666}],[{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"remove","lines":[" "],"id":667},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":[" "]},{"start":{"row":17,"column":4},"end":{"row":18,"column":2},"action":"remove","lines":["","  "]}],[{"start":{"row":217,"column":4},"end":{"row":217,"column":8},"action":"remove","lines":["    "],"id":668},{"start":{"row":217,"column":0},"end":{"row":217,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":217,"column":0},"end":{"row":218,"column":0},"action":"insert","lines":["",""],"id":669}],[{"start":{"row":218,"column":0},"end":{"row":218,"column":27},"action":"insert","lines":["teardown_test_environment()"],"id":670}],[{"start":{"row":218,"column":27},"end":{"row":219,"column":0},"action":"insert","lines":["",""],"id":671},{"start":{"row":219,"column":0},"end":{"row":220,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":[","],"id":672}],[{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":[" "],"id":673},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["t"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["e"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["a"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["r"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"insert","lines":["_"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"insert","lines":["o"],"id":674},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"insert","lines":["w"]},{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"insert","lines":["n"]},{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"insert","lines":[")"]}],[{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"remove","lines":[")"],"id":675}],[{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"insert","lines":["_"],"id":676},{"start":{"row":1,"column":64},"end":{"row":1,"column":65},"action":"insert","lines":["t"]},{"start":{"row":1,"column":65},"end":{"row":1,"column":66},"action":"insert","lines":["e"]},{"start":{"row":1,"column":66},"end":{"row":1,"column":67},"action":"insert","lines":["s"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"insert","lines":["t"]},{"start":{"row":1,"column":68},"end":{"row":1,"column":69},"action":"insert","lines":["_"]},{"start":{"row":1,"column":69},"end":{"row":1,"column":70},"action":"insert","lines":["e"]},{"start":{"row":1,"column":70},"end":{"row":1,"column":71},"action":"insert","lines":["n"]},{"start":{"row":1,"column":71},"end":{"row":1,"column":72},"action":"insert","lines":["v"]}],[{"start":{"row":1,"column":72},"end":{"row":1,"column":73},"action":"insert","lines":["i"],"id":677},{"start":{"row":1,"column":73},"end":{"row":1,"column":74},"action":"insert","lines":["r"]},{"start":{"row":1,"column":74},"end":{"row":1,"column":75},"action":"insert","lines":["o"]},{"start":{"row":1,"column":75},"end":{"row":1,"column":76},"action":"insert","lines":["n"]},{"start":{"row":1,"column":76},"end":{"row":1,"column":77},"action":"insert","lines":["m"]},{"start":{"row":1,"column":77},"end":{"row":1,"column":78},"action":"insert","lines":["e"]},{"start":{"row":1,"column":78},"end":{"row":1,"column":79},"action":"insert","lines":["n"]},{"start":{"row":1,"column":79},"end":{"row":1,"column":80},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":678}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":679}],[{"start":{"row":0,"column":32},"end":{"row":1,"column":80},"action":"remove","lines":["","from django.test.utils import setup_test_environment, tear_down_test_environment"],"id":680}],[{"start":{"row":216,"column":0},"end":{"row":217,"column":27},"action":"remove","lines":["","teardown_test_environment()"],"id":681}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":24},"action":"remove","lines":["","setup_test_environment()"],"id":682},{"start":{"row":2,"column":30},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":[","],"id":683}],[{"start":{"row":12,"column":40},"end":{"row":12,"column":66},"action":"insert","lines":["{'name': 'fred', 'age': 7}"],"id":684}],[{"start":{"row":12,"column":42},"end":{"row":12,"column":46},"action":"remove","lines":["name"],"id":685},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["b"]},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"insert","lines":["m"]},{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"insert","lines":["i"]}],[{"start":{"row":12,"column":45},"end":{"row":12,"column":46},"action":"insert","lines":["_"],"id":686},{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"insert","lines":["r"]},{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"insert","lines":["e"]},{"start":{"row":12,"column":48},"end":{"row":12,"column":49},"action":"insert","lines":["s"]},{"start":{"row":12,"column":49},"end":{"row":12,"column":50},"action":"insert","lines":["u"]},{"start":{"row":12,"column":50},"end":{"row":12,"column":51},"action":"insert","lines":["l"]},{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":55},"end":{"row":12,"column":61},"action":"remove","lines":["'fred'"],"id":687},{"start":{"row":12,"column":55},"end":{"row":12,"column":56},"action":"insert","lines":["2"]},{"start":{"row":12,"column":56},"end":{"row":12,"column":57},"action":"insert","lines":["2"]},{"start":{"row":12,"column":57},"end":{"row":12,"column":58},"action":"insert","lines":["."]},{"start":{"row":12,"column":58},"end":{"row":12,"column":59},"action":"insert","lines":["5"]}],[{"start":{"row":12,"column":59},"end":{"row":12,"column":60},"action":"insert","lines":["0"],"id":688}],[{"start":{"row":12,"column":63},"end":{"row":12,"column":66},"action":"remove","lines":["age"],"id":689},{"start":{"row":12,"column":63},"end":{"row":12,"column":64},"action":"insert","lines":["b"]},{"start":{"row":12,"column":64},"end":{"row":12,"column":65},"action":"insert","lines":["m"]},{"start":{"row":12,"column":65},"end":{"row":12,"column":66},"action":"insert","lines":["i"]},{"start":{"row":12,"column":66},"end":{"row":12,"column":67},"action":"insert","lines":["_"]},{"start":{"row":12,"column":67},"end":{"row":12,"column":68},"action":"insert","lines":["c"]},{"start":{"row":12,"column":68},"end":{"row":12,"column":69},"action":"insert","lines":["a"]},{"start":{"row":12,"column":69},"end":{"row":12,"column":70},"action":"insert","lines":["t"]},{"start":{"row":12,"column":70},"end":{"row":12,"column":71},"action":"insert","lines":["e"]},{"start":{"row":12,"column":71},"end":{"row":12,"column":72},"action":"insert","lines":["g"]}],[{"start":{"row":12,"column":72},"end":{"row":12,"column":73},"action":"insert","lines":["o"],"id":690},{"start":{"row":12,"column":73},"end":{"row":12,"column":74},"action":"insert","lines":["r"]},{"start":{"row":12,"column":74},"end":{"row":12,"column":75},"action":"insert","lines":["y"]}],[{"start":{"row":12,"column":78},"end":{"row":12,"column":79},"action":"remove","lines":["7"],"id":691},{"start":{"row":12,"column":78},"end":{"row":12,"column":79},"action":"insert","lines":["'"]},{"start":{"row":12,"column":79},"end":{"row":12,"column":80},"action":"insert","lines":["'"]}],[{"start":{"row":12,"column":79},"end":{"row":12,"column":80},"action":"insert","lines":["h"],"id":692},{"start":{"row":12,"column":80},"end":{"row":12,"column":81},"action":"insert","lines":["e"]},{"start":{"row":12,"column":81},"end":{"row":12,"column":82},"action":"insert","lines":["l"]},{"start":{"row":12,"column":82},"end":{"row":12,"column":83},"action":"insert","lines":["a"]},{"start":{"row":12,"column":83},"end":{"row":12,"column":84},"action":"insert","lines":["t"]},{"start":{"row":12,"column":84},"end":{"row":12,"column":85},"action":"insert","lines":["h"]},{"start":{"row":12,"column":85},"end":{"row":12,"column":86},"action":"insert","lines":["u"]},{"start":{"row":12,"column":86},"end":{"row":12,"column":87},"action":"insert","lines":["y"]}],[{"start":{"row":12,"column":86},"end":{"row":12,"column":87},"action":"remove","lines":["y"],"id":693},{"start":{"row":12,"column":85},"end":{"row":12,"column":86},"action":"remove","lines":["u"]},{"start":{"row":12,"column":84},"end":{"row":12,"column":85},"action":"remove","lines":["h"]},{"start":{"row":12,"column":83},"end":{"row":12,"column":84},"action":"remove","lines":["t"]},{"start":{"row":12,"column":82},"end":{"row":12,"column":83},"action":"remove","lines":["a"]},{"start":{"row":12,"column":81},"end":{"row":12,"column":82},"action":"remove","lines":["l"]}],[{"start":{"row":12,"column":81},"end":{"row":12,"column":82},"action":"insert","lines":["a"],"id":694},{"start":{"row":12,"column":82},"end":{"row":12,"column":83},"action":"insert","lines":["l"]},{"start":{"row":12,"column":83},"end":{"row":12,"column":84},"action":"insert","lines":["t"]},{"start":{"row":12,"column":84},"end":{"row":12,"column":85},"action":"insert","lines":["h"]},{"start":{"row":12,"column":85},"end":{"row":12,"column":86},"action":"insert","lines":["y"]}],[{"start":{"row":2,"column":30},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":695},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":28},"action":"insert","lines":["from django.test.utils import setup_test_environment",">>> setup_test_environment()"],"id":696}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":[">>> "],"id":697},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":51},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":698},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]},{"start":{"row":19,"column":8},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":699}],[{"start":{"row":20,"column":4},"end":{"row":26,"column":44},"action":"insert","lines":["    def test_whatever_list_view(self):","        w = self.create_whatever()","        url = reverse(\"whatever.views.whatever\")","        resp = self.client.get(url)","","        self.assertEqual(resp.status_code, 200)","        self.assertIn(w.title, resp.content)"],"id":700}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":701}],[{"start":{"row":20,"column":38},"end":{"row":21,"column":34},"action":"remove","lines":["","        w = self.create_whatever()"],"id":702}],[{"start":{"row":2,"column":30},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":703},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":704},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["."]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["v"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["i"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["w"],"id":705},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":706},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["i"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["m"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["p"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["o"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["e"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["r"],"id":707},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["e"]}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["r"],"id":708},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[" "],"id":709},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["b"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["i"]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":22},"action":"remove","lines":["bmi"],"id":710},{"start":{"row":3,"column":19},"end":{"row":3,"column":29},"action":"insert","lines":["bmi_result"]}],[{"start":{"row":21,"column":38},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":711},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["b"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["m"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["i"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":11},"action":"remove","lines":["bmi"],"id":712},{"start":{"row":22,"column":8},"end":{"row":22,"column":20},"action":"insert","lines":["bmi_result()"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["b"],"id":713},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["m"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["i"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["_"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["r"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["e"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["s"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["u"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["l"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":[" "],"id":714},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":[" "],"id":715}],[{"start":{"row":3,"column":29},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":716}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":73},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, redirect, reverse"],"id":717}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":31},"action":"remove","lines":["whatever"],"id":718}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":38},"action":"remove","lines":["whatever"],"id":719},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["b"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["m"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["i"]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":33},"action":"remove","lines":["bmi"],"id":720},{"start":{"row":24,"column":30},"end":{"row":24,"column":40},"action":"insert","lines":["bmi_result"]}],[{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"remove","lines":["_"],"id":721},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"remove","lines":["i"]},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"remove","lines":["m"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":22,"column":38},"end":{"row":23,"column":29},"action":"remove","lines":["","        result = bmi_result()"],"id":722}],[{"start":{"row":26,"column":47},"end":{"row":27,"column":44},"action":"remove","lines":["","        self.assertIn(w.title, resp.content)"],"id":723}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":51},"action":"remove","lines":["        response = c.get('/bmi_result/',{'bmi_result': 22.50, 'bmi_category': 'healthy'})","        self.assertEqual(response.status_code, 200)"],"id":724}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["#"],"id":725}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":726}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":727}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":728},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":729},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":8},"action":"remove","lines":["    "],"id":730},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "],"id":731}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":8},"action":"insert","lines":["    "],"id":732}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":733},{"start":{"row":20,"column":8},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":734}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":735}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":736},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["d"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":[" "],"id":737},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["t"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["e"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["s"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":738}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":12},"action":"remove","lines":["    ","    def test"],"id":739}],[{"start":{"row":5,"column":0},"end":{"row":8,"column":24},"action":"remove","lines":["","from django.test.utils import setup_test_environment","","setup_test_environment()"],"id":740}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1597755302342,"hash":"e84fc219018a257a46abb708408cc0b1c59ee224"}