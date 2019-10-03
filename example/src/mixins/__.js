export default {
  name: 'CreateAppointmentForm',

  computed: {
    ...mapGetters({
      doctor: 'doctors/getDoctor',
    }),
    messageRules: function () {
      return [
        value => !!value || this.$i18n.t('rules.required.from.js'),
        value => value.length >= 20 || this.$i18n.t('rules.minChar20.from.js')
      ]
    },
  }
}
