<template>
  <v-card flat>
    <v-card-title>
      <h3>{{$t('modals.appointment.header')}}</h3>
      <h5 v-show="this.$vuetify.breakpoint.xsOnly">{{ $t('modals.appointment.doctor', {name: this.doctor.name}) }}</h5>
    </v-card-title>
    <v-card-text>
      <v-text-field
        :label="$t('modals.appointment.dateLabel')"
        :rules="messageRules"
      ></v-text-field>
    </v-card-text>
    <p> {{ tc('appointment', {count: this.doctor.appointmentCount}) }}</p>
  </v-card>
</template>

<script>
  export default {
    name: 'CreateAppointmentForm',

    computed: {
      ...mapGetters({
        doctor: 'doctors/getDoctor',
      }),
      messageRules: function () {
        return [
          value => !!value || this.$i18n.t('rules.required'),
          value => value.length >= 20 || this.$i18n.t('rules.minChar20')
        ]
      },
    }

  };
</script>

