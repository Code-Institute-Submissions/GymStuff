{"filter":false,"title":"tests.py","tooltip":"/physical/tests.py","undoManager":{"mark":94,"position":94,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.test import TestCase","","# Create your tests here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":21,"column":13},"action":"insert","lines":["from django.test import TestCase","from .models import Product","","# Product model tests.","class ProductTests(TestCase):","    ","    # Test setup by creating new products","    def setUp(self):","        Product.objects.create(","            name=\"10kg weight\", ","            category=\"Weights\", ","            short_description=\"A weight plate\",","            description=\"A light weight plate\",","            price =\"50.00\"","            )","        Product.objects.create(","            name=\"pull up bar\", ","            category=\"Accessories\", ","            short_description=\"A pull up bar\",","            description=\"A door mounted pull up bar\",","            price =\"30.00\"","            )"]}],[{"start":{"row":1,"column":21},"end":{"row":1,"column":27},"action":"remove","lines":["roduct"],"id":3},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["h"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["y"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["s"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["i"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["c"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["a"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["l"]}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":23,"column":0},"end":{"row":28,"column":60},"action":"insert","lines":["    def test_animals_can_speak(self):","        \"\"\"Animals that can speak are correctly identified\"\"\"","        lion = Animal.objects.get(name=\"lion\")","        cat = Animal.objects.get(name=\"cat\")","        self.assertEqual(lion.speak(), 'The lion says \"roar\"')","        self.assertEqual(cat.speak(), 'The cat says \"meow\"')"],"id":5}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":41},"action":"remove","lines":["products"],"id":6},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["b"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["m"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["i"]}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":[" "],"id":7},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["m"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["o"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["d"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["e"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":42},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":9},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"remove","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"remove","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":6,"column":42},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":10}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":11},{"start":{"row":6,"column":42},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":[","],"id":12}],[{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":[" "],"id":13},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["M"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["a"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["c"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["r"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":13},"action":"remove","lines":["Product"],"id":14},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["B"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["M"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["I"]}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":9},"action":"remove","lines":["Product"],"id":15},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["B"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["M"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["I"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":15},"action":"remove","lines":["roduct"],"id":16},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["h"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["y"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["s"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["i"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["c"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["a"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["l"]}],[{"start":{"row":21,"column":13},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":22,"column":0},"end":{"row":22,"column":12},"action":"insert","lines":["            "]},{"start":{"row":22,"column":12},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":12},"action":"insert","lines":["            "]},{"start":{"row":23,"column":12},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":12},"action":"insert","lines":["            "]},{"start":{"row":24,"column":12},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":25,"column":12},"end":{"row":34,"column":4},"action":"insert","lines":["    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)","    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)","    unit_height = models.FloatField(default=0)","    unit_weight = models.FloatField(default=0)","    bmi_calc = models.FloatField(default=0)","    bmi_category = models.CharField(default='', max_length=200)","    date_now = models.DateTimeField(auto_now_add=True)","    unit_type = models.CharField(choices=unit_type, default='Metric', max_length=200)","    "],"id":18}],[{"start":{"row":9,"column":0},"end":{"row":13,"column":26},"action":"remove","lines":["            name=\"10kg weight\", ","            category=\"Weights\", ","            short_description=\"A weight plate\",","            description=\"A light weight plate\",","            price =\"50.00\""],"id":19},{"start":{"row":9,"column":0},"end":{"row":17,"column":85},"action":"insert","lines":["                user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)","    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)","    unit_height = models.FloatField(default=0)","    unit_weight = models.FloatField(default=0)","    bmi_calc = models.FloatField(default=0)","    bmi_category = models.CharField(default='', max_length=200)","    date_now = models.DateTimeField(auto_now_add=True)","    unit_type = models.CharField(choices=unit_type, default='Metric', max_length=200)"]}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":16},"action":"remove","lines":["    "],"id":20},{"start":{"row":9,"column":8},"end":{"row":9,"column":12},"action":"remove","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":21},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":22},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":88},"action":"remove","lines":["            user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)"],"id":23},{"start":{"row":8,"column":32},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":98},"action":"remove","lines":["models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)"],"id":24},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["1"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["6"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["0"]}],[{"start":{"row":10,"column":21},"end":{"row":10,"column":98},"action":"remove","lines":["models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)"],"id":25},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["8"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["0"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["'"],"id":26}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["'"],"id":27}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":[","],"id":28}],[{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":[","],"id":29}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":54},"action":"remove","lines":[" models.FloatField(default=0)"],"id":30},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":[" "]}],[{"start":{"row":11,"column":26},"end":{"row":11,"column":53},"action":"insert","lines":["calculate_unit_height(self)"],"id":31}],[{"start":{"row":11,"column":53},"end":{"row":11,"column":54},"action":"insert","lines":[","],"id":32}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":54},"action":"remove","lines":["models.FloatField(default=0)"],"id":33},{"start":{"row":12,"column":26},"end":{"row":12,"column":53},"action":"insert","lines":["calculate_unit_height(self)"]}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":["h"],"id":34}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["w"],"id":35}],[{"start":{"row":12,"column":53},"end":{"row":12,"column":54},"action":"insert","lines":[","],"id":36}],[{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"insert","lines":[","],"id":37}],[{"start":{"row":14,"column":71},"end":{"row":14,"column":72},"action":"insert","lines":[","],"id":38}],[{"start":{"row":14,"column":72},"end":{"row":15,"column":62},"action":"remove","lines":["","            date_now = models.DateTimeField(auto_now_add=True)"],"id":39}],[{"start":{"row":15,"column":93},"end":{"row":15,"column":94},"action":"insert","lines":[","],"id":40}],[{"start":{"row":15,"column":93},"end":{"row":15,"column":94},"action":"remove","lines":[","],"id":41}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":51},"action":"remove","lines":["models.FloatField(default=0)"],"id":42},{"start":{"row":13,"column":23},"end":{"row":13,"column":43},"action":"insert","lines":["calculated_bmi(self)"]}],[{"start":{"row":14,"column":27},"end":{"row":14,"column":71},"action":"remove","lines":["models.CharField(default='', max_length=200)"],"id":43},{"start":{"row":14,"column":27},"end":{"row":14,"column":46},"action":"insert","lines":["category_calc(self)"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":93},"action":"remove","lines":["models.CharField(choices=unit_type, default='Metric', max_length=200)"],"id":44},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["'"]}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["m"],"id":45}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["m"],"id":46}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["M"],"id":47},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["e"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["t"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["r"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["i"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["'"],"id":48}],[{"start":{"row":17,"column":0},"end":{"row":23,"column":13},"action":"remove","lines":["        Product.objects.create(","            name=\"pull up bar\", ","            category=\"Accessories\", ","            short_description=\"A pull up bar\",","            description=\"A door mounted pull up bar\",","            price =\"30.00\"","            )"],"id":49}],[{"start":{"row":17,"column":0},"end":{"row":29,"column":85},"action":"remove","lines":["","            ","            ","            ","                user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)","    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)","    unit_height = models.FloatField(default=0)","    unit_weight = models.FloatField(default=0)","    bmi_calc = models.FloatField(default=0)","    bmi_category = models.CharField(default='', max_length=200)","    date_now = models.DateTimeField(auto_now_add=True)","    unit_type = models.CharField(choices=unit_type, default='Metric', max_length=200)"],"id":50}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":51}],[{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["s"],"id":52},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["e"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["l"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["f"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":26},"end":{"row":11,"column":30},"action":"remove","lines":["self"],"id":53},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["P"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["h"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["y"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["s"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["i"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["c"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["a"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["l"]}],[{"start":{"row":11,"column":57},"end":{"row":11,"column":61},"action":"remove","lines":["self"],"id":54}],[{"start":{"row":11,"column":0},"end":{"row":14,"column":47},"action":"remove","lines":["            unit_height = Physical.calculate_unit_height(),","            unit_weight = calculate_unit_weight(self),","            bmi_calc = calculated_bmi(self),","            bmi_category = category_calc(self),"],"id":56}],[{"start":{"row":21,"column":60},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]},{"start":{"row":22,"column":8},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":8},"end":{"row":26,"column":47},"action":"insert","lines":["            unit_height = Physical.calculate_unit_height(),","            unit_weight = calculate_unit_weight(self),","            bmi_calc = calculated_bmi(self),","            bmi_category = category_calc(self),"],"id":58}],[{"start":{"row":23,"column":16},"end":{"row":23,"column":20},"action":"remove","lines":["    "],"id":59},{"start":{"row":23,"column":12},"end":{"row":23,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":24},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":60}],[{"start":{"row":12,"column":13},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":13,"column":0},"end":{"row":13,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":12},"action":"remove","lines":["    "],"id":62}],[{"start":{"row":13,"column":8},"end":{"row":17,"column":13},"action":"insert","lines":["        Physical.objects.create(","            height = 160,","            weight = 80,","            unit_type = 'Metric'","            )"],"id":63}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":16},"action":"remove","lines":["    "],"id":64},{"start":{"row":13,"column":8},"end":{"row":13,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":23},"action":"remove","lines":["16"],"id":65},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["8"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["8"],"id":66}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["2"],"id":67},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["0"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":20},"action":"remove","lines":["animals"],"id":68},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["c"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["L"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["C"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["U"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["L"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["A"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["T"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["E"]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["E"],"id":69},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["T"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["A"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["L"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["U"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["C"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["L"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["a"],"id":70},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["l"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["c"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["u"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["l"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["a"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["t"]},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":26},"action":"remove","lines":["can"],"id":71},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["u"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["n"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["i"]},{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":33},"action":"remove","lines":["speak"],"id":72},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["h"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["e"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["i"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["g"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["h"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"remove","lines":["lion"],"id":73},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["m"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["e"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["t"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["r"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["i"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["c"]}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":23},"action":"remove","lines":["Animal"],"id":74},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["P"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["h"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["y"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["s"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":["i"]},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["c"]},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["a"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["l"]}],[{"start":{"row":16,"column":25},"end":{"row":16,"column":31},"action":"remove","lines":["Metric"],"id":75},{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"insert","lines":["I"]},{"start":{"row":16,"column":26},"end":{"row":16,"column":27},"action":"insert","lines":["m"]},{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"insert","lines":["p"]},{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"insert","lines":["e"]},{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"insert","lines":["r"]},{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"insert","lines":["i"]},{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"insert","lines":["a"]},{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["l"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":58},"action":"remove","lines":["Animals that can speak are correctly identified"],"id":76},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["B"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["m"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["i"]}],[{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":[" "],"id":77},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["c"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["o"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["r"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["r"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["e"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["c"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["t"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["l"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["y"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":[" "],"id":78},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["c"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["l"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["c"]},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["u"]},{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["l"]},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["a"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["t"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["e"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":42},"action":"remove","lines":["name"],"id":79},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["u"]},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["n"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["i"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":42},"action":"remove","lines":["unit"],"id":80},{"start":{"row":22,"column":38},"end":{"row":22,"column":47},"action":"insert","lines":["unit_type"]}],[{"start":{"row":22,"column":49},"end":{"row":22,"column":53},"action":"remove","lines":["lion"],"id":81},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"insert","lines":["M"]},{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"insert","lines":["e"]},{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"insert","lines":["t"]},{"start":{"row":22,"column":52},"end":{"row":22,"column":53},"action":"insert","lines":["r"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"insert","lines":["i"]},{"start":{"row":22,"column":54},"end":{"row":22,"column":55},"action":"insert","lines":["c"]}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":11},"action":"remove","lines":["cat"],"id":82},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["i"]},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":["m"]},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":["e"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["r"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["p"]}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["p"],"id":83},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"remove","lines":["r"]},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"remove","lines":["e"]}],[{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":["p"],"id":84},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["e"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["r"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["i"]},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["a"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["l"]}],[{"start":{"row":23,"column":19},"end":{"row":23,"column":49},"action":"remove","lines":["Animal.objects.get(name=\"cat\")"],"id":85},{"start":{"row":23,"column":19},"end":{"row":23,"column":59},"action":"insert","lines":["Physical.objects.get(unit_type=\"Metric\")"]}],[{"start":{"row":23,"column":56},"end":{"row":23,"column":57},"action":"remove","lines":["c"],"id":86},{"start":{"row":23,"column":55},"end":{"row":23,"column":56},"action":"remove","lines":["i"]},{"start":{"row":23,"column":54},"end":{"row":23,"column":55},"action":"remove","lines":["r"]},{"start":{"row":23,"column":53},"end":{"row":23,"column":54},"action":"remove","lines":["t"]},{"start":{"row":23,"column":52},"end":{"row":23,"column":53},"action":"remove","lines":["e"]},{"start":{"row":23,"column":51},"end":{"row":23,"column":52},"action":"remove","lines":["M"]}],[{"start":{"row":23,"column":51},"end":{"row":23,"column":52},"action":"insert","lines":["I"],"id":87},{"start":{"row":23,"column":52},"end":{"row":23,"column":53},"action":"insert","lines":["m"]},{"start":{"row":23,"column":53},"end":{"row":23,"column":54},"action":"insert","lines":["p"]},{"start":{"row":23,"column":54},"end":{"row":23,"column":55},"action":"insert","lines":["e"]},{"start":{"row":23,"column":55},"end":{"row":23,"column":56},"action":"insert","lines":["r"]},{"start":{"row":23,"column":56},"end":{"row":23,"column":57},"action":"insert","lines":["i"]},{"start":{"row":23,"column":57},"end":{"row":23,"column":58},"action":"insert","lines":["a"]},{"start":{"row":23,"column":58},"end":{"row":23,"column":59},"action":"insert","lines":["l"]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":35},"action":"remove","lines":["speak"],"id":88},{"start":{"row":24,"column":30},"end":{"row":24,"column":44},"action":"insert","lines":["calculated_bmi"]}],[{"start":{"row":25,"column":29},"end":{"row":25,"column":34},"action":"remove","lines":["speak"],"id":89},{"start":{"row":25,"column":29},"end":{"row":25,"column":43},"action":"insert","lines":["calculated_bmi"]}],[{"start":{"row":24,"column":25},"end":{"row":24,"column":29},"action":"remove","lines":["lion"],"id":90},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["m"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["e"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["t"]},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["r"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["i"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["c"]}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":28},"action":"remove","lines":["cat"],"id":91},{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["i"]},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["m"]},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["p"]},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["e"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["r"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["i"]},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["a"]},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["l"]}],[{"start":{"row":24,"column":51},"end":{"row":24,"column":71},"action":"remove","lines":["The lion says \"roar\""],"id":92},{"start":{"row":24,"column":51},"end":{"row":24,"column":56},"action":"insert","lines":["31.25"]}],[{"start":{"row":25,"column":53},"end":{"row":25,"column":72},"action":"remove","lines":["The cat says \"meow\""],"id":93},{"start":{"row":25,"column":53},"end":{"row":25,"column":54},"action":"insert","lines":["2"]},{"start":{"row":25,"column":54},"end":{"row":25,"column":55},"action":"insert","lines":["2"]},{"start":{"row":25,"column":55},"end":{"row":25,"column":56},"action":"insert","lines":["."]},{"start":{"row":25,"column":56},"end":{"row":25,"column":57},"action":"insert","lines":["0"]},{"start":{"row":25,"column":57},"end":{"row":25,"column":58},"action":"insert","lines":["4"]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["#"],"id":94}],[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["#"],"id":95}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["#"],"id":96}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["#"],"id":97}]]},"ace":{"folds":[],"scrolltop":7,"scrollleft":0,"selection":{"start":{"row":16,"column":34},"end":{"row":16,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1597669829543,"hash":"c7349a005604a949702e3d785a1bff7ec7a4746a"}