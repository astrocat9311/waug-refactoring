CSV_PATH_PRODUCTS = 'conveniences.csv'
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)


            for row in data_reader:
                Convenience.objects.create(
                    name = row[1],
                    service_type_id =  fake.pyint(min_value=1, max_value=7, step=1),
                )

    #class Command(BaseCommand):
#    def add_arguments(self, parser):
#        parser.add_argument(
#            '--total',
#            default=2,
#            type=int,
#            help='this is test'
#        )
#
#
#    def handle(self,*args, **options):
#        total    = int(options.get("total"))
#        seeder   = Seed.seeder()
#        fake     = Faker(["ko_KR"])

        #seeder.add_entity(
        #    City,
        #    total,
        #    {
        #        'name': lambda x: fake.unique.city()
        #
        #
        #       # 'user'        : lambda x: random.choice(users),
        #       # "user_address": lambda x: fake.unique.address(),
        #       # "is_default"  : False
        #    }
        #)

       #CSV_PATH_PRODUCTS = './service_types.csv'
       #with open(CSV_PATH_PRODUCTS) as in_file:
       #    data_reader = csv.reader(in_file)
       #    next(data_reader, None)
       #
       #    for row in data_reader:
       #        ServiceType.objects.create(
       #            name=row[1],
       #        )

        #인스턴트의 execute()메서드로 실행!
        #seeder.execute()
        #성공하면 메세지
        #self.stdout.write(self.style.SUCCESS(f"{total} users created!"))