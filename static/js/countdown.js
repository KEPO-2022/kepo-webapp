const countDown = () => {
  const countDate = new Date("January 17, 2022 00:00:00").getTime(); //Set waktu untuk akhir countdown
  const now = new Date().getTime(); //Set waktu untuk saat ini
  const gap = countDate - now; // Hitung selisih waktu dalam ms

  // Cara perhitungan waktu tiap 1 satuan ke milisecond
  const second = 1000;
  const minute = second * 60;
  const hour = minute * 60;
  const day = hour * 24;

  // Hitung Waktu
  // Hari
  const textDay = Math.floor(gap / day);
  const daysSatuan = textDay % 10;
  const daysPuluhan = Math.floor(textDay / 10);
  // Jam
  const textHour = Math.floor((gap % day) / hour);
  const hoursSatuan = textHour % 10;
  const hoursPuluhan = Math.floor(textHour / 10);
  // Menit
  const textMinute = Math.floor((gap % hour) / minute);
  const minutesSatuan = textMinute % 10;
  const minutesPuluhan = Math.floor(textMinute / 10);
  // Detik
  const textSecond = Math.floor((gap % minute) / second);
  const secondSatuan = textSecond % 10;
  const secondPuluhan = Math.floor(textSecond / 10);

  if (gap >= 0) {
    // Hari
    document.querySelector(".days .puluhan").innerText = daysPuluhan;
    document.querySelector(".days .satuan").innerText = daysSatuan;
    // Jam
    document.querySelector(".hours .puluhan").innerText = hoursPuluhan;
    document.querySelector(".hours .satuan").innerText = hoursSatuan;
    // Menit
    document.querySelector(".minutes .puluhan").innerText = minutesPuluhan;
    document.querySelector(".minutes .satuan").innerText = minutesSatuan;
    // Detik
    document.querySelector(".seconds .puluhan").innerText = secondPuluhan;
    document.querySelector(".seconds .satuan").innerText = secondSatuan;
  } else {
    // Hari
    document.querySelector(".days .puluhan").innerText = 0;
    document.querySelector(".days .satuan").innerText = 0;
    // Jam
    document.querySelector(".hours .puluhan").innerText = 0;
    document.querySelector(".hours .satuan").innerText = 0;
    // Menit
    document.querySelector(".minutes .puluhan").innerText = 0;
    document.querySelector(".minutes .satuan").innerText = 0;
    // Detik
    document.querySelector(".seconds .puluhan").innerText = 0;
    document.querySelector(".seconds .satuan").innerText = 0;
  }

  return gap;
};

if (countDown() >= 0) {
  setInterval(countDown, 1000);
} else {
  clearInterval(countDown);
  $(".countdown-display").css("display", "none");
}
