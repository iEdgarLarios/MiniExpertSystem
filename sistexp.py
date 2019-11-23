from experta import *


class DeployQuestion(Fact):
    pass


class PlatformPicker(KnowledgeEngine):
    @Rule(DeployQuestion(app_size="small",
                         app_type=L("Rails") | L("Node") | L("Laravel"),
                         app_require_specific_infrastructure="no",
                         have_enough_money="no",
                         know_about_infrastructure="no",
                         will_you_app_grow_up_soon="no",
                         app_needs_multiple_services="no",
                         want_a_vpn="no",
                         app_has_specific_dependencies="no",
                         want_container_orchestration="no"
                         ))
    def you_better_use_heroku(self):
        print("Heroku is for you")

    @Rule(DeployQuestion(app_size=L("medium") | L("small"),
                         app_type=L("Rails") | L("Node") | L("Laravel") | L("None"),
                         app_require_specific_infrastructure=L("yes") | L("no"),
                         have_enough_money=L("no") | L("yes"),
                         know_about_infrastructure=L("yes") | L("no"),
                         will_you_app_grow_up_soon=L("no") | L("yes"),
                         app_needs_multiple_services=L("no") | L("yes"),
                         want_a_vpn=L("no") | L("yes"),
                         app_has_specific_dependencies=L("no") | "yes",
                         want_container_orchestration=L("no") | L("yes")
                         ))
    def you_better_use_digital_ocean(self):
        print("Digital Ocean is for you")

    @Rule(DeployQuestion(app_size=L("medium") | L("big"),
                         app_type=L("Rails") | L("Node") | L("Laravel") | L("None"),
                         app_require_specific_infrastructure="yes",
                         have_enough_money=L("no") | L("yes"),
                         know_about_infrastructure="yes",
                         will_you_app_grow_up_soon=L("no") | L("yes"),
                         app_needs_multiple_services=L("no") | L("yes"),
                         want_a_vpn=L("no") | L("yes"),
                         app_has_specific_dependencies=L("no") | "yes",
                         want_container_orchestration=L("no") | L("yes")
                         ))
    def you_better_use_aws(self):
        print("AWS is for you")

    @Rule(DeployQuestion(app_size=L("medium") | L("big"),
                         app_type=L("Rails") | L("Node") | L("Laravel") | L("None"),
                         app_require_specific_infrastructure=L("yes") | L("no"),
                         have_enough_money=L("no") | L("yes"),
                         know_about_infrastructure=L("yes") | L("no"),
                         will_you_app_grow_up_soon=L("no") | L("yes"),
                         app_needs_multiple_services=L("no") | L("yes"),
                         want_a_vpn=L("no") | L("yes"),
                         app_has_specific_dependencies=L("no") | "yes",
                         want_container_orchestration=L("no") | L("yes")
                         ))
    def you_better_use_google(self):
        print("Google Cloud is for you")

app_size = input("Your app is mall, medium, big:" )
app_type = input("Your app uses Rails, Node, Laravel, None" )
app_require_specific_infrastructure = input("Your app uses a specific infrastructure: ")
have_enough_money = input("Do you have enough money for your app? ")
know_about_infrastructure = input("Do you know about infrastructures: ")
will_you_app_grow_up_soon = input("Will your app exponentially wrog up soon? ")
app_needs_multiple_services = input("Does your app need multiple external services? ")
want_a_vpn = input("Do you need a VPN: ")
app_has_specific_dependencies = input("Does your app need specific dependencies? ")
want_container_orchestration = input("Dou you need to orchestrate containers? ")

engine = PlatformPicker()
engine.reset()
engine.declare(DeployQuestion(app_size=app_size, app_type=app_type, app_require_specific_infrastructure=app_require_specific_infrastructure,
                              have_enough_money=have_enough_money, know_about_infrastructure=know_about_infrastructure,
                              will_you_app_grow_up_soon=will_you_app_grow_up_soon, app_needs_multiple_services=app_needs_multiple_services,
                              want_a_vpn=want_a_vpn, app_has_specific_dependencies=app_has_specific_dependencies,
                              want_container_orchestration=want_container_orchestration))
engine.run()