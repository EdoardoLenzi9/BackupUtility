
import Utils.document_parser as parser
import Services.backup_service as backup_svc

def main():
    backup_svc.print_message("Welcome to BackUp-Utility by dodo")
    directives = parser.parse_config("settings.config")
    directives = backup_svc.apply_config(directives)
    backup_svc.generate_scripts(directives)

main()