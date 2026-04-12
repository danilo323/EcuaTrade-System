const productos = [
  {
    id: 5,
    vendedor: "vendedor_juan",
    nombre_producto: 'Mouse Gamer Inalámbrico "EcuaSwift" RGB',
    precio: "32.50",
    stock: 15,
    badge: "NEW",
    imagen: "http://127.0.0.1:8000/media/productos/78a21e19-b9b3-4638-889c-79a97de35efd.png"
  },
  {
    id: 6,
    vendedor: "vendedor_juan",
    nombre_producto: 'Microfono Gamer "Babahoyo Sound" Pro (Rojo)',
    precio: "39.99",
    stock: 29,
    badge: "HOT",
    imagen: "http://127.0.0.1:8000/media/productos/12314064-9d0b-47bf-bf1d-a7f405457423.avif"
  },
  {
    id: 7,
    vendedor: "vendedor_juan",
    nombre_producto: 'Teclado Mecánico TKL "Andes Pro" (Teclas Blancas)',
    precio: "58.00",
    stock: 23,
    imagen: "http://127.0.0.1:8000/media/productos/798353ad-949d-41fc-9193-77acf0aa7367.avif"
  },
  {
    id: 8,
    vendedor: "vendedor_juan",
    nombre_producto: "Adaptador doble HDMI 2.5",
    precio: "12.00",
    stock: 45,
    imagen: "http://127.0.0.1:8000/media/productos/5a6a9463-c062-46a8-82cd-2c351a2430ea.avif"
  },
  {
    id: 9,
    vendedor: "vendedor_juan",
    nombre_producto: "M.2 SSD DATA 512 GB",
    precio: "90.00",
    stock: 30,
    badge: "NEW",
    imagen: "http://127.0.0.1:8000/media/productos/15911428-cea8-4de0-9469-72c7d499360c.avif"
  },
  {
    id: 10,
    vendedor: "vendedor_juan",
    nombre_producto: 'Deskmat / Mousepad XL "Guayas Black',
    precio: "15.00",
    stock: 28,
    imagen: "http://127.0.0.1:8000/media/productos/733108d276ad4ae2878012d1ee94f0fb-goods.avif"
  },
  {
    id: 11,
    vendedor: "vendedor_juan",
    nombre_producto: "Wirelees Game Control - PC",
    precio: "25.00",
    stock: 11,
    imagen: "http://127.0.0.1:8000/media/productos/6bedf176-f8c5-47b8-86fd-fe60adf40323.avif"
  },
  {
    id: 12,
    vendedor: "vendedor_juan",
    nombre_producto: "Teclado mecánico Negro, KLC Rainwobd",
    precio: "39.99",
    stock: 27,
    imagen: "http://127.0.0.1:8000/media/productos/5d746409-221e-4e37-94c5-17c3122b4ca3.avif"
  },
  {
    id: 13,
    vendedor: "vendedor_juan",
    nombre_producto: 'Control Inalámbrico "Chimborazo Elite"',
    precio: "49.99",
    stock: 32,
    imagen: null
  },
  {
    id: 14,
    vendedor: "vendedor_juan",
    nombre_producto: 'Mando Multiplataforma "Tungurahua Play" Bluetooth',
    precio: "39.99",
    stock: 39,
    badge: "HOT",
    imagen: "http://127.0.0.1:8000/media/productos/14102bf5-9832-4905-84e4-401cd7e1c8c6.avif"
  }
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