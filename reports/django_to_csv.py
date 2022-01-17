

# export model to csv
def export_people(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tof_users.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'First Name', 'Last Name', 'Is Member', 'Is leader','group'])
    user = queryset.values_list('username', 'first_name', 'last_name', 'is_member', 'is_leader','group')
    for users in user:
        writer.writerow(users)
    return response
export_people.short_description = 'Export to csv'
