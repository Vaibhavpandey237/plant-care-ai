export const INITIAL_PLANTS = [
  {
    id: "monstera-deliciosa",
    name: "Monstera Deliciosa",
    scientificName: "Monstera deliciosa",
    category: "Indoor",
    image: "/images/monstera.png",
    waterFrequencyDays: 7,
    light: "Bright Indirect",
    humidity: "60-80%",
    temperature: "18-30°C",
    toxicity: "Toxic to Pets 🐾",
    isPetSafe: false,
    isLowLight: false,
    isAirPurifying: true,
    difficulty: "Easy",
    description: "Iconic tropical plant famous for its large, glossy leaves featuring beautiful natural split patterns (fenestrations). Native to the tropical forests of Central America.",
    careTips: [
      "Wipe leaves with a damp cloth monthly to remove dust.",
      "Provide a moss pole or trellis for support as it grows climbing aerial roots.",
      "Water thoroughly when top 2 inches of soil feel completely dry."
    ]
  },
  {
    id: "snake-plant",
    name: "Snake Plant (Sansevieria)",
    scientificName: "Sansevieria trifasciata",
    category: "Air Purifying",
    image: "/images/snake_plant.png",
    waterFrequencyDays: 14,
    light: "Low to Bright Indirect",
    humidity: "30-50%",
    temperature: "15-29°C",
    toxicity: "Mildly Toxic to Pets 🐾",
    isPetSafe: false,
    isLowLight: true,
    isAirPurifying: true,
    difficulty: "Beginner",
    description: "Extremely resilient architectural plant with stiff, upright sword-like leaves. Outstanding oxygen producer and bedroom air purifier.",
    careTips: [
      "Tolerates neglect very well. Better to underwater than overwater.",
      "Use well-draining cactus or succulent soil mix.",
      "Can thrive in low-light corners and windowless offices."
    ]
  },
  {
    id: "peace-lily",
    name: "Peace Lily",
    scientificName: "Spathiphyllum wallisii",
    category: "Flowering",
    image: "/images/peace_lily.png",
    waterFrequencyDays: 5,
    light: "Medium Indirect",
    humidity: "50-70%",
    temperature: "18-26°C",
    toxicity: "Toxic to Cats & Dogs 🐾",
    isPetSafe: false,
    isLowLight: true,
    isAirPurifying: true,
    difficulty: "Easy",
    description: "Lush dark green foliage that blooms elegant white spathes. Known for dramatically drooping when thirsty and rebounding within hours after watering.",
    careTips: [
      "Keep soil consistently moist but never waterlogged.",
      "Prune spent white flowers at the base of the stem.",
      "Mist leaves or place near a humidifier to keep leaf tips crisp and green."
    ]
  },
  {
    id: "calathea-orbifolia",
    name: "Calathea Orbifolia",
    scientificName: "Goeppertia orbifolia",
    category: "Indoor",
    image: "/images/calathea.png",
    waterFrequencyDays: 6,
    light: "Medium Indirect",
    humidity: "65-80%",
    temperature: "18-24°C",
    toxicity: "Pet Safe 🐶🐱",
    isPetSafe: true,
    isLowLight: false,
    isAirPurifying: true,
    difficulty: "Intermediate",
    description: "Breathtaking prayer plant with enormous, round leaves displaying metallic silver stripes. Folds its leaves upward at night like praying hands.",
    careTips: [
      "Use filtered, distilled, or rainwater to avoid mineral leaf burn.",
      "Keep humidity high (60%+); avoid placement near heating vents or drafty windows.",
      "Never allow soil to dry out completely."
    ]
  }
];
