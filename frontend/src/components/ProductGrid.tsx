const productos = [
  {
    id: 5,
    nombre_producto: 'Mouse Gamer Inalámbrico "EcuaSwift" RGB',
    precio: "32.50",
    stock: 15,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400&h=400&fit=crop",
  },
  {
    id: 6,
    nombre_producto: 'Micrófono Gamer "Babahoyo Sound" Pro (Rojo)',
    precio: "39.99",
    stock: 29,
    badge: "HOT",
    imagen: "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=400&h=400&fit=crop",
  },
  {
    id: 7,
    nombre_producto: 'Teclado Mecánico TKL "Andes Pro" (Teclas Blancas)',
    precio: "58.00",
    stock: 23,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=400&h=400&fit=crop",
  },
  {
    id: 8,
    nombre_producto: "Adaptador doble HDMI 2.5",
    precio: "12.00",
    stock: 45,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1625842268584-8f3296236761?w=400&h=400&fit=crop",
  },
  {
    id: 9,
    nombre_producto: "M.2 SSD DATA 512 GB",
    precio: "90.00",
    stock: 30,
    badge: "NEW",
    imagen: "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400&h=400&fit=crop",
  },
  {
    id: 10,
    nombre_producto: 'Deskmat / Mousepad XL "Guayas Black"',
    precio: "15.00",
    stock: 28,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1616788494707-ec28f08d05a1?w=400&h=400&fit=crop",
  },
  {
    id: 11,
    nombre_producto: "Wireless Game Control — PC",
    precio: "25.00",
    stock: 11,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=400&h=400&fit=crop",
  },
  {
    id: 12,
    nombre_producto: "Teclado Mecánico Negro KLC Rainwood",
    precio: "39.99",
    stock: 27,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1595225476474-87563907a212?w=400&h=400&fit=crop",
  },
  {
    id: 13,
    nombre_producto: 'Control Inalámbrico "Chimborazo Elite"',
    precio: "49.99",
    stock: 32,
    badge: "",
    imagen: "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=400&h=400&fit=crop",
  },
  {
    id: 14,
    nombre_producto: 'Mando Multiplataforma "Tungurahua Play" Bluetooth',
    precio: "39.99",
    stock: 39,
    badge: "HOT",
    imagen: "https://images.unsplash.com/photo-1605901309584-818e25960a8f?w=400&h=400&fit=crop",
  },
];

const ProductGrid = () => {
  return (
    <section className="bg-slate-50 px-8 py-10">
      {/* Header de sección */}
      <div className="flex items-center justify-between mb-8">
        <h2 className="text-xl font-bold text-slate-800 flex items-center gap-3">
          <span className="w-1 h-6 bg-sky-400 rounded-full inline-block" />
          Productos destacados
        </h2>
        <button className="text-sky-500 text-sm hover:text-sky-400 transition-colors">
          Ver todos →
        </button>
      </div>

      {/* Grid de productos */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        {productos.map((prod) => (
          <div
            key={prod.id}
            className="bg-white border border-slate-100 rounded-xl overflow-hidden hover:shadow-lg hover:-translate-y-1 transition-all duration-200 flex flex-col relative cursor-pointer"
          >
            {/* Badge */}
            {prod.badge && (
              <span
                className={`absolute top-2 left-2 z-10 text-white text-xs font-semibold px-2 py-0.5 rounded ${
                  prod.badge === "NEW" ? "bg-emerald-500" : "bg-red-500"
                }`}
              >
                {prod.badge}
              </span>
            )}

            {/* Imagen */}
            <div className="h-36 bg-slate-50 flex items-center justify-center p-3">
              <img
                src={prod.imagen || "https://placehold.co/300x300?text=Sin+Imagen"}
                alt={prod.nombre_producto}
                className="max-h-full max-w-full object-contain rounded"
                loading="lazy"
              />
            </div>

            {/* Info */}
            <div className="p-3 flex flex-col flex-1">
              <h3 className="text-sm font-semibold text-slate-800 leading-snug line-clamp-2 mb-2 flex-1">
                {prod.nombre_producto}
              </h3>

              <div className="mt-auto">
                <p className="text-sky-600 font-bold text-lg">${prod.precio}</p>
                <p className={`text-xs mb-3 ${prod.stock < 15 ? "text-red-400" : "text-slate-400"}`}>
                  Stock: {prod.stock} unidades
                </p>
                <button className="w-full bg-slate-900 text-white py-2 rounded-lg text-xs font-semibold hover:bg-sky-400 hover:text-slate-900 transition-colors duration-200">
                  Añadir al carrito
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProductGrid;
